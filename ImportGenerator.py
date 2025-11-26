"""
Import Generator Tool

This module provides functionality to scan a directory for Python files,
extract import statements, resolve aliases, and generate a consolidated,
duplicate-free list of imports.

Usage:
    python import_generator.py /path/to/your/tests --output unique_imports.py
"""

import ast
import argparse
import os
import sys
from collections import defaultdict
from typing import Dict, List, Set, Tuple


class ImportGenerator:
    """Generates a unique set of import statements from a directory of Python files."""

    def __init__(self, target_folder_path: str):
        """
        Initializes the ImportGenerator.

        Args:
            target_folder_path: The root directory to scan for Python files.
        """
        self.target_folder_path = target_folder_path
        # Stores fully formatted 'from ... import ...' statements
        self.import_statements: Set[str] = set()
        # Maps module names to a set of aliases found in the code
        self.module_aliases: Dict[str, Set[str]] = defaultdict(set)
        # Tracks aliases that have already been assigned to avoid conflicts
        self.used_aliases: Set[str] = set()

    def process_files(self) -> List[str]:
        """
        Scans all Python files in the target directory, extracts imports,
        and returns a sorted list of unique import statements.

        Returns:
            A list of unique, valid Python import strings.
        """
        if not os.path.exists(self.target_folder_path):
            print(f"Error: Directory not found: {self.target_folder_path}", file=sys.stderr)
            return []

        for root, _, files in os.walk(self.target_folder_path):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    self._extract_imports_from_file(file_path)

        return self._generate_unique_imports()

    def _extract_imports_from_file(self, file_path: str) -> None:
        """
        Parses a single Python file using AST to extract import statements.

        Args:
            file_path: The absolute path to the Python file.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()

            tree = ast.parse(file_content)

            for node in ast.walk(tree):
                # Handle: import xxx [as yyy]
                if isinstance(node, ast.Import):
                    for name in node.names:
                        module_name = name.name
                        # If no alias is provided, the alias is the module name (or last part of it)
                        alias = name.asname or module_name.split('.')[-1]
                        
                        self.module_aliases[module_name].add(alias)
                        self.used_aliases.add(alias)

                # Handle: from xxx import yyy [as zzz]
                elif isinstance(node, ast.ImportFrom):
                    # node.module is None for relative imports (e.g., 'from . import func')
                    # We exclude these as they may not work in the generated standalone context
                    if node.module is not None:
                        module_name = node.module
                        for name in node.names:
                            imported_name = name.name
                            alias = name.asname or imported_name

                            import_str = f"from {module_name} import {imported_name}"
                            if name.asname:
                                import_str += f" as {alias}"

                            self.import_statements.add(import_str)
                            self.used_aliases.add(alias)

        except SyntaxError:
            print(f"Skipping file due to syntax error: {file_path}", file=sys.stderr)
        except Exception as e:
            print(f"Error processing file {file_path}: {e}", file=sys.stderr)

    def _generate_unique_imports(self) -> List[str]:
        """
        Resolves alias conflicts and generates the final list of import statements.

        Returns:
            A sorted list of import statements.
        """
        result = list(self.import_statements)

        # Local tracking for this generation phase to resolve conflicts
        resolved_aliases = set()
        alias_counter = defaultdict(int)

        # Process 'import xxx' style imports
        # Sorting ensures deterministic output
        for module, aliases in sorted(self.module_aliases.items()):
            # Logic: If multiple aliases exist for a module, prioritize the one 
            # that matches the module's name (last segment).
            preferred_alias = module.split('.')[-1]

            if preferred_alias in aliases and preferred_alias not in resolved_aliases:
                chosen_alias = preferred_alias
            else:
                # Fallback: Generate a unique alias if the preferred one is taken
                base_alias = module.split('.')[-1]
                chosen_alias = base_alias

                # Increment counter until a unique alias is found
                if chosen_alias in resolved_aliases:
                    alias_counter[base_alias] += 1
                    chosen_alias = f"{base_alias}_{alias_counter[base_alias]}"

            resolved_aliases.add(chosen_alias)

            # Construct the final statement
            # If the alias matches the module name, no 'as' keyword is needed
            if chosen_alias == module.split('.')[-1]:
                result.append(f"import {module}")
            else:
                result.append(f"import {module} as {chosen_alias}")

        return sorted(result)

    def save_imports_to_file(self, output_file: str) -> None:
        """
        Generates imports and writes them to a file.

        Args:
            output_file: Path to the output file.
        """
        imports = self.process_files()
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("# Auto-generated import list\n\n")
                for import_stmt in imports:
                    f.write(f"{import_stmt}\n")
            print(f"Successfully saved {len(imports)} imports to {output_file}")
        except IOError as e:
            print(f"Error writing to output file: {e}", file=sys.stderr)


def main():
    """Main entry point for command line usage."""
    parser = argparse.ArgumentParser(description="Extract and consolidate imports from a Python project.")
    
    parser.add_argument(
        "target_dir", 
        help="Path to the directory containing Python files to scan."
    )
    parser.add_argument(
        "--output", "-o",
        default="consolidated_imports.py",
        help="Path for the output file (default: consolidated_imports.py)"
    )

    args = parser.parse_args()

    # Normalize path
    target_path = os.path.abspath(args.target_dir)

    generator = ImportGenerator(target_path)
    
    # Save to file
    generator.save_imports_to_file(args.output)


if __name__ == "__main__":
    main()