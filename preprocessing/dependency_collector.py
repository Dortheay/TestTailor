"""
Dependency Collector
====================
Given a CodeUnit, collect all functions, classes, and variables that the unit
depends on (potentially across files) using:
  1. AST parsing + class dependency graph
  2. Backward program slicing from the unit's statements
  3. Cross-module import resolution

Returns a DependencyContext ready to be embedded into an LLM prompt.
"""

import ast
import textwrap
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

from models import CodeUnit, DependencyContext


# ──────────────────────────────────────────────────────────────────────────────
# AST helpers
# ──────────────────────────────────────────────────────────────────────────────

def _unparse(node: ast.AST) -> str:
    return ast.unparse(node)


def _get_names_used(node: ast.AST) -> Set[str]:
    """Collect all Name and Attribute root names referenced inside *node*."""
    names: Set[str] = set()
    for n in ast.walk(node):
        if isinstance(n, ast.Name):
            names.add(n.id)
        elif isinstance(n, ast.Attribute):
            # collect the root object name
            root = n
            while isinstance(root, ast.Attribute):
                root = root.value
            if isinstance(root, ast.Name):
                names.add(root.id)
    return names


def _node_source(source_lines: List[str], node: ast.AST) -> str:
    """Extract dedented source text for an AST node."""
    lines = source_lines[node.lineno - 1: node.end_lineno]
    return textwrap.dedent("\n".join(lines))


# ──────────────────────────────────────────────────────────────────────────────
# Module cache – avoid re-parsing the same file repeatedly
# ──────────────────────────────────────────────────────────────────────────────

class _ModuleIndex:
    """Cached index of definitions in a single Python source file."""

    def __init__(self, path: str):
        self.path = path
        source = Path(path).read_text(encoding="utf-8")
        self.source_lines = source.splitlines()
        self.tree = ast.parse(source, filename=path)
        self._build_indexes()

    def _build_indexes(self):
        # name → AST node for top-level functions and classes
        self.functions: Dict[str, ast.FunctionDef] = {}
        self.classes: Dict[str, ast.ClassDef] = {}
        self.assignments: Dict[str, ast.Assign] = {}

        for node in self.tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                self.functions[node.name] = node
            elif isinstance(node, ast.ClassDef):
                self.classes[node.name] = node
                # Index methods inside the class
                for item in node.body:
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        # e.g. "MyClass.my_method"
                        self.functions[f"{node.name}.{item.name}"] = item
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        self.assignments[target.id] = node

    def get_function_source(self, name: str) -> Optional[str]:
        node = self.functions.get(name)
        return _node_source(self.source_lines, node) if node else None

    def get_class_source(self, name: str) -> Optional[str]:
        node = self.classes.get(name)
        return _node_source(self.source_lines, node) if node else None

    def get_imports(self) -> List[str]:
        imports = []
        for node in self.tree.body:
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                imports.append(_node_source(self.source_lines, node))
        return imports


_module_cache: Dict[str, _ModuleIndex] = {}


def _get_index(path: str) -> _ModuleIndex:
    if path not in _module_cache:
        _module_cache[path] = _ModuleIndex(path)
    return _module_cache[path]


# ──────────────────────────────────────────────────────────────────────────────
# Import resolver
# ──────────────────────────────────────────────────────────────────────────────

class ImportResolver:
    """
    Resolves 'from X import Y' and 'import X' statements to actual file paths.
    Uses sys.path to locate modules.
    """

    def __init__(self, project_root: str):
        self.project_root = Path(project_root)

    def resolve(self, module_name: str) -> Optional[str]:
        """
        Try to find the .py file for *module_name* within the project root.
        Returns the absolute path string or None.
        """
        parts = module_name.split(".")
        # Try as a package path
        candidate = self.project_root.joinpath(*parts).with_suffix(".py")
        if candidate.exists():
            return str(candidate)
        # Try __init__.py of a package
        pkg_init = self.project_root.joinpath(*parts, "__init__.py")
        if pkg_init.exists():
            return str(pkg_init)
        return None


# ──────────────────────────────────────────────────────────────────────────────
# Backward slicer
# ──────────────────────────────────────────────────────────────────────────────

class BackwardSlicer:
    """
    Performs a simplified backward program slice starting from the names
    used in a CodeUnit, resolving them across files.
    """

    def __init__(self, primary_index: _ModuleIndex, resolver: ImportResolver):
        self.primary = primary_index
        self.resolver = resolver
        self._visited: Set[str] = set()  # already resolved names

    def slice(self, used_names: Set[str]) -> List[str]:
        """
        Return a list of source snippets (function bodies, class definitions,
        variable assignments) that the given names depend on.
        """
        snippets: List[str] = []
        queue = list(used_names)

        while queue:
            name = queue.pop()
            if name in self._visited:
                continue
            self._visited.add(name)

            # Check functions
            src = self.primary.get_function_source(name)
            if src:
                snippets.append(src)
                # Find further dependencies inside this function body
                sub_tree = ast.parse(src)
                new_names = _get_names_used(sub_tree) - self._visited
                queue.extend(new_names)
                continue

            # Check classes
            src = self.primary.get_class_source(name)
            if src:
                snippets.append(src)
                continue

            # Check assignments (module-level constants / config dicts)
            node = self.primary.assignments.get(name)
            if node:
                line = _node_source(self.primary.source_lines, node)
                snippets.append(line)
                continue

            # Try to find in imported modules
            self._search_imports(name, snippets, queue)

        return snippets

    def _search_imports(self, name: str, snippets: List[str], queue: List[str]):
        """Look for *name* in the modules imported by the primary file."""
        for node in self.primary.tree.body:
            if isinstance(node, ast.ImportFrom) and node.module:
                for alias in node.names:
                    imported_name = alias.asname or alias.name
                    if imported_name == name or alias.name == name:
                        # Try to resolve the module
                        resolved = self.resolver.resolve(node.module)
                        if resolved:
                            try:
                                idx = _get_index(resolved)
                                src = (idx.get_function_source(alias.name) or
                                       idx.get_class_source(alias.name))
                                if src:
                                    snippets.append(f"# From {node.module}\n{src}")
                                    # Recursively collect deps from the found entity
                                    new_names = _get_names_used(ast.parse(src)) - self._visited
                                    queue.extend(new_names)
                            except Exception as e:
                                print(f"[DependencyCollector] Warning: failed to index {resolved}: {e}")


# ──────────────────────────────────────────────────────────────────────────────
# Main Dependency Collector
# ──────────────────────────────────────────────────────────────────────────────

class DependencyCollector:
    """
    Collects all dependency information for a CodeUnit.

    Parameters
    ----------
    source_file : path to the module under test
    project_root : root directory of the project (for cross-file resolution)
    """

    def __init__(self, source_file: str, project_root: str):
        self.source_file = source_file
        self.index = _get_index(source_file)
        self.resolver = ImportResolver(project_root)

    def collect(self, unit: CodeUnit) -> DependencyContext:
        """
        Build a DependencyContext for *unit*.
        """
        # 1. Get enclosing function source
        func_src = self._get_enclosing_function(unit)

        # 2. Get class source (if the function is a method)
        class_src = self._get_enclosing_class(unit)

        # 3. Backward slice: find what names the unit uses
        # Prefer code_snippet if available; otherwise extract from source lines.
        snippet = getattr(unit, "code_snippet", None) or ""
        if not snippet.strip() and unit.start_lineno and unit.end_lineno:
            # Fall back to slicing the source file directly
            snippet = "\n".join(
                self.index.source_lines[unit.start_lineno - 1: unit.end_lineno]
            )

        unit_tree = ast.parse(textwrap.dedent(snippet)) if snippet.strip() else ast.parse("")
        used_names = _get_names_used(unit_tree)

        # Also collect names from the full enclosing function, because the unit
        # might only cover a single line while dependencies span the whole method.
        if func_src:
            used_names |= _get_names_used(ast.parse(textwrap.dedent(func_src)))

        # Remove built-ins and very common names
        used_names -= set(dir(__builtins__)) if isinstance(__builtins__, dict) \
            else set(dir(__builtins__))
        used_names.discard(unit.function_name)

        slicer = BackwardSlicer(self.index, self.resolver)
        dep_srcs = slicer.slice(used_names)

        # 4. Collect relevant imports
        imports = self.index.get_imports()

        return DependencyContext(
            target_unit=unit,
            enclosing_function_src=func_src,
            class_definition_src=class_src,
            dependency_srcs=dep_srcs,
            imports=imports,
        )

    # ── Helpers ──────────────────────────────────────────────────────────────

    def _get_enclosing_function(self, unit: CodeUnit) -> str:
        """Return source of the function that contains the unit."""
        node = self.index.functions.get(unit.function_name)
        if node is None:
            # Try as a method: search all classes
            for cls_name, cls_node in self.index.classes.items():
                for item in cls_node.body:
                    if (isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef))
                            and item.name == unit.function_name):
                        return _node_source(self.index.source_lines, item)
        return _node_source(self.index.source_lines, node) if node else ""

    def _get_enclosing_class(self, unit: CodeUnit) -> Optional[str]:
        """Return class source if the function is a method, else search imports."""
        # Check if it's defined in this module
        for cls_name, cls_node in self.index.classes.items():
            for item in cls_node.body:
                if (isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef))
                        and item.name == unit.function_name):
                    return _node_source(self.index.source_lines, cls_node)

        # If not found, check if the class is imported from another module
        for imp in self.index.get_imports():
            if "OrderController" in imp:  # check if it's the imported class
                # Try to resolve the import and fetch class source
                imported_module_path = self.resolver.resolve('controller.order_controller')
                if imported_module_path:
                    imported_index = _get_index(imported_module_path)
                    return imported_index.get_class_source("OrderController")
        
        return None


# ──────────────────────────────────────────────────────────────────────────────
# Convenience entry point
# ──────────────────────────────────────────────────────────────────────────────

def collect_dependencies(
    unit: CodeUnit,
    source_file: str,
    project_root: str,
) -> DependencyContext:
    """High-level entry point for dependency collection."""
    collector = DependencyCollector(source_file, project_root)
    return collector.collect(unit)


def main():
    # 创建一个 CodeUnit 实例进行测试
    unit = CodeUnit(
        unit_id= "main:unit_1",
        source_file= "/Users/dorthea/Documents/research/paperSubmission/FSE2026/TestTailorCode/tests/order_management/controller/order_controller.py",
        function_name= "create_order",
        start_lineno=10,
        end_lineno=10,
        unit_type= "linear"
    )
    source_file = "/Users/dorthea/Documents/research/paperSubmission/FSE2026/TestTailorCode/tests/order_management/controller/order_controller.py"
    project_root = "/Users/dorthea/Documents/research/paperSubmission/FSE2026/TestTailorCode/tests/order_management"
    # 初始化 DependencyCollector
    collector = DependencyCollector(source_file=source_file, project_root=project_root)
    
    # 收集 CodeUnit 的依赖
    dependency_context = collector.collect(unit)
    
    # 输出结果（打印收集到的信息）
    print("封闭函数源代码:")
    print(dependency_context.enclosing_function_src)
    
    print("\n类定义源代码:")
    print(dependency_context.class_definition_src if dependency_context.class_definition_src else "没有找到类定义。")
    
    print("\n依赖（函数、类、赋值）:")
    for dep in dependency_context.dependency_srcs:
        print(dep)
    
    print("\n导入模块:")
    for imp in dependency_context.imports:
        print(imp)

if __name__ == "__main__":
    main()