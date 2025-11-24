import ast
from pathlib import Path
from typing import Dict, Any, List


class ProjectClassIndexer:
    """
    Custom class indexer for the project
    Scan the entire project and extract all class definitions, support querying complete class information by class name
    """

    def __init__(self, project_root: str):
        self.project_root = Path(project_root).absolute()
        self.class_index: Dict[str, Dict[str, Any]] = {}
        self._build_index()

    def _build_index(self):
        """Scan the project directory, build the class index"""
        for py_file in self.project_root.rglob("*.py"):
            if "test" in py_file.name.lower():
                continue
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    source = f.read()
                tree = ast.parse(source)

                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        start_line = node.lineno
                        end_line = self._find_class_end(node, source)
                        docstring = ast.get_docstring(node)
                        init_method = self._find_init_method(node,source)

                        self.class_index[node.name] = {
                            "name": node.name,
                            "file": str(py_file),
                            "start_line": start_line,
                            "end_line": end_line,
                            "docstring": docstring,
                            "init_method": init_method,
                        }
            except Exception as e:
                print(f"[WARN] Error parsing {py_file}: {e}")

    def _find_class_end(self, class_node: ast.ClassDef, source: str) -> int:
        """Roughly find the end line number of the class"""
        lines = source.splitlines()
        start_line = class_node.lineno
        indent = len(lines[start_line - 1]) - len(lines[start_line - 1].lstrip())

        for i in range(start_line, len(lines)):
            line = lines[i]
            if line.strip() and not line.startswith(" ") and not line.startswith("\t"):
                return i
            # If the indentation decreases, it means the class ends
            if line.strip() and (len(line) - len(line.lstrip())) <= indent and i > start_line:
                return i
        return len(lines)

    def _find_init_method(self, class_node: ast.ClassDef, source: str) -> str:
        """Extract the class definition + __init__ method source code"""
        lines = source.splitlines()
        init_node = None

        # Find the __init__ node
        for node in class_node.body:
            if isinstance(node, ast.FunctionDef) and node.name == "__init__":
                init_node = node
                break

        if not init_node:
            return ""  # If there is no __init__ method, return empty

        # class start line (ast.lineno starts from 1, so subtract 1)
        start_line = class_node.lineno - 1

        # __init__ method end line (Python 3.8+ has end_lineno)
        end_line = getattr(init_node, "end_lineno", None)
        if end_line is None:
            # If Python < 3.8, you need to infer it yourself
            init_start = init_node.lineno - 1
            indent = len(lines[init_start]) - len(lines[init_start].lstrip())
            for i in range(init_start + 1, len(lines)):
                line = lines[i]
                if line.strip() and (len(line) - len(line.lstrip())) <= indent:
                    end_line = i
                    break
            else:
                end_line = len(lines)

        return "\n".join(lines[start_line:end_line])



    def get_class_info(self, class_name: str) -> Dict[str, Any]:
        """Get the complete information of the specified class (with source code snippet)"""
        if class_name not in self.class_index:
            return {}

        cls = self.class_index[class_name]
        with open(cls["file"], "r", encoding="utf-8") as f:
            lines = f.readlines()

        cls_code = "".join(lines[cls["start_line"] - 1:cls["end_line"]])
        cls_info = {
            **cls,
            "code": cls_code
        }
        return cls_info

    def search_classes(self, keywords: List[str]) -> List[Dict[str, Any]]:
        """Search classes by keywords"""
        result = []
        for name, info in self.class_index.items():
            if any(kw in name for kw in keywords):
                result.append(info)
        return result


if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Test the ProjectClassIndexer")
    parser.add_argument("project_root", help="Path to the project root directory")
    parser.add_argument("--search", nargs="*", help="Class name keywords to search", default=[])
    parser.add_argument("--show", help="Show specific class source code", default=None)

    args = parser.parse_args()

    indexer = ProjectClassIndexer(args.project_root)

    print("===== Indexed Classes =====")
    for cls_name, info in indexer.class_index.items():
        print(f"- {cls_name} (file: {info['file']}, line: {info['start_line']}-{info['end_line']})")

    if args.search:
        print("\n===== Search Result =====")
        results = indexer.search_classes(args.search)
        for r in results:
            print(json.dumps(r, indent=2, ensure_ascii=False))

    if args.show:
        print(f"\n===== Class Detail: {args.show} =====")
        detail = indexer.get_class_info(args.show)
        if detail:
            print(json.dumps({k: v for k, v in detail.items() if k != "code"}, indent=2, ensure_ascii=False))
            print("\n--- Class Source Code ---\n")
            print(detail["code"])
        else:
            print(f"Class {args.show} not found.")
