"""
Static Code Analysis Tool for Python

This module provides tools for analyzing Python code execution paths,
performing symbolic execution, and extracting variable usage.

Dependencies:
    - python_code_structure_parser (Custom module)
"""

import argparse
import ast
import csv
import datetime
import json
import os
import re
from typing import Any, Dict, List, Optional, Set, Tuple

# Assuming python_code_structure_parser is available in the Python path
from python_code_structure_parser import Node, PythonCodeParser

# Constant: Python keywords and built-ins for variable extraction filtering
_PYTHON_KEYWORDS = {
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
    'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
    'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
    'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield',
    'print', 'len', 'range', 'int', 'str', 'list', 'dict', 'set', 'tuple',
    'bool', 'float', 'complex', 'bytes', 'bytearray', 'memoryview', 'object',
    'enumerate', 'filter', 'map', 'zip', 'reversed', 'sorted', 'sum', 'any', 'all',
    'min', 'max', 'abs', 'round', 'pow', 'divmod', 'isinstance', 'issubclass',
    'hasattr', 'getattr', 'setattr', 'delattr', 'callable', 'iter', 'next',
    'open', 'input', 'repr', 'chr', 'ord', 'bin', 'oct', 'hex', 'id', 'hash'
}


class PathAnalyzer:
    """Analyzes execution paths within the code structure."""

    def __init__(self, parser: PythonCodeParser):
        self.parser = parser

    def get_contextual_execution_path(self, target_node: Node) -> Dict[str, Any]:
        """
        Retrieves the execution path for a target node, including context about loops and conditions.

        Args:
            target_node: The node to analyze.

        Returns:
            A dictionary containing the main path with context and potential alternative paths.
        """
        main_path = self.parser.get_execution_path(target_node)
        
        contextual_info = []
        for node in main_path:
            info = {"node": node, "context": []}
            
            if node.condition:
                info["context"].append(f"Condition: {node.condition}")
            
            if node.node_type in ['for', 'while']:
                info["context"].append("This is a loop that may execute multiple times")
            
            if node.node_type in ['if', 'elif', 'else']:
                for child in node.children:
                    if child.node_type in ['break', 'return', 'continue']:
                        info["context"].append(f"May exit early via {child.node_type}")
            
            contextual_info.append(info)
        
        # Generate alternative paths based on control flow siblings
        alternative_paths = self._generate_alternative_paths(main_path)
        
        return {
            "main_path": contextual_info,
            "alternative_paths": alternative_paths
        }

    def _generate_alternative_paths(self, main_path: List[Node]) -> List[Dict[str, Any]]:
        """Generates alternative execution paths based on sibling control structures."""
        alternative_paths = []
        
        for i, node in enumerate(main_path):
            if node.node_type in ['if', 'elif', 'else']:
                siblings = self.parser.get_siblings(node)
                condition_siblings = [s for s in siblings 
                                    if s.node_type in ['if', 'elif', 'else']]
                
                for sibling in condition_siblings:
                    # Construct a new path where the sibling is taken instead
                    alt_path = main_path[:i] + [sibling]
                    description = (f"Alternative path if '{sibling.condition or sibling.code}' "
                                 f"is taken instead of '{node.condition or node.code}'")
                    
                    alternative_paths.append({
                        "path": alt_path,
                        "description": description
                    })
        
        return alternative_paths


class SymbolicExecutor:
    """Performs basic symbolic execution to determine path constraints."""

    def __init__(self, parser: PythonCodeParser):
        self.parser = parser

    def get_path_constraints(self, target_node: Node) -> List[Tuple[Node, str, bool]]:
        """
        Collects constraints (conditions) required to reach the target node.

        Returns:
            A list of tuples: (Node, condition_string, is_positive_assertion).
        """
        path = self.parser.get_execution_path(target_node)
        constraints = []
        
        for node in path:
            if node.node_type == 'if' and node.condition:
                constraints.append((node, node.condition, True))
            
            elif node.node_type in ['elif', 'else']:
                chain = self._get_if_elif_chain(node)
                
                # Add negated constraints for previous siblings in the chain
                for chain_node in chain:
                    if (chain_node.line_number < node.line_number and 
                        chain_node.condition):
                        negated = self._negate_condition(chain_node.condition)
                        constraints.append((chain_node, negated, False))
                
                # Add the positive constraint for the current node (if any)
                if node.condition:
                    constraints.append((node, node.condition, True))
            
            elif node.node_type in ['while', 'for'] and node.condition:
                constraints.append((node, node.condition, True))
        
        return constraints

    def _get_if_elif_chain(self, node: Node) -> List[Node]:
        """Retrieves the full chain of if/elif/else blocks related to the node."""
        siblings = self.parser.get_siblings(node)
        chain = [s for s in siblings if s.node_type in ('if', 'elif', 'else')]
        
        if node not in chain:
            chain.append(node)
        
        return sorted(chain, key=lambda n: n.line_number)

    def _negate_condition(self, condition: str) -> str:
        """
        Negates a condition string.
        Note: This uses simple string replacement and may not cover complex expressions.
        """
        if not condition:
            return ""
        
        negation_map = {
            " == ": " != ", " != ": " == ",
            " > ": " <= ", " < ": " >= ",
            " >= ": " < ", " <= ": " > ",
            "True": "False", "False": "True"
        }
        
        for original, negated in negation_map.items():
            if original in condition:
                return condition.replace(original, negated)
        
        return f"not ({condition})"

    def _combine_constraints(self, constraints: List[Tuple[Node, str, bool]]) -> str:
        """Combines multiple constraints into a single logical string."""
        if not constraints:
            return "No constraints found."
        
        positive = [f"({cond})" for _, cond, is_pos in constraints if is_pos]
        negative = [f"({cond})" for _, cond, is_pos in constraints if not is_pos]
        
        parts = []
        if positive:
            parts.append(" and ".join(positive))
        if negative:
            parts.append(" and ".join(negative))
        
        return " and ".join(parts)

    def analyze_path(self, target_node: Node) -> Dict[str, Any]:
        """Performs full symbolic analysis on the path to the target node."""
        execution_path = self.parser.get_execution_path(target_node)
        path_constraints = self.get_path_constraints(target_node)
        
        return {
            "target_node": target_node,
            "execution_path": execution_path,
            "path_constraints": path_constraints,
            "combined_constraint": self._combine_constraints(path_constraints)
        }


class VariableAnalyzer:
    """Analyzes variable usage and extraction from code snippets."""

    @staticmethod
    def extract_variables_from_code(code: str) -> Dict[str, Any]:
        """
        Extracts variable names and array accesses from a code string.
        Tries AST parsing first, then falls back to Regex.
        """
        individual_vars = set()
        array_accesses = set()
        
        try:
            # Attempt AST parsing
            tree = ast.parse(code.strip())
            
            class VariableVisitor(ast.NodeVisitor):
                def visit_Name(self, node):
                    # Visit variable names
                    if node.id not in _PYTHON_KEYWORDS:
                        individual_vars.add(node.id)
                    self.generic_visit(node)
                
                def visit_Subscript(self, node):
                    # Visit array/dict access e.g., arr[0]
                    if isinstance(node.value, ast.Name):
                        var_name = node.value.id
                        if var_name not in _PYTHON_KEYWORDS:
                            individual_vars.add(var_name)
                            try:
                                full_access = ast.unparse(node)
                                array_accesses.add(full_access)
                            except AttributeError:
                                # For older Python versions where ast.unparse might not be available
                                array_accesses.add(f"{var_name}[...]")
                    elif isinstance(node.value, ast.Subscript):
                        try:
                            full_access = ast.unparse(node)
                            array_accesses.add(full_access)
                        except AttributeError:
                            pass
                    self.generic_visit(node)
                
                def visit_Attribute(self, node):
                    # Visit attribute access e.g., obj.attr
                    if isinstance(node.value, ast.Name):
                        var_name = node.value.id
                        if var_name not in _PYTHON_KEYWORDS:
                            individual_vars.add(var_name)
                            try:
                                full_access = ast.unparse(node)
                                array_accesses.add(full_access)
                            except AttributeError:
                                array_accesses.add(f"{var_name}.{node.attr}")
                    self.generic_visit(node)
            
            visitor = VariableVisitor()
            visitor.visit(tree)
            
        except SyntaxError:
            # Fallback to Regex if AST parsing fails
            # print(f"AST parsing failed for: {code}, falling back to regex")
            
            # Clean code: remove comments and strings
            code_clean = re.sub(r'#.*$', '', code)
            code_clean = re.sub(r'""".*?"""', '', code_clean, flags=re.DOTALL)
            code_clean = re.sub(r"'''.*?'''", '', code_clean, flags=re.DOTALL)
            code_clean = re.sub(r'"(?:[^"\\]|\\.)*"', '', code_clean)
            code_clean = re.sub(r"'(?:[^'\\]|\\.)*'", '', code_clean)
            
            # Regex for array/attribute access
            array_pattern = r'([a-zA-Z_][a-zA-Z0-9_]*(?:\[[^\]]+\])+)'
            array_matches = re.findall(array_pattern, code_clean)
            for match in array_matches:
                array_accesses.add(match)
                base_var = re.match(r'([a-zA-Z_][a-zA-Z0-9_]*)', match)
                if base_var:
                    individual_vars.add(base_var.group(1))
            
            # Regex for attributes
            attr_pattern = r'([a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)*)'
            attr_matches = re.findall(attr_pattern, code_clean)
            for match in attr_matches:
                array_accesses.add(match)
                base_var = match.split('.')[0]
                individual_vars.add(base_var)
            
            # Regex for basic variables
            variable_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
            potential_vars = re.findall(variable_pattern, code_clean)
            
            for var in potential_vars:
                if var not in _PYTHON_KEYWORDS:
                    # Exclude function calls
                    func_call_pattern = rf'\b{re.escape(var)}\s*\('
                    if not re.search(func_call_pattern, code):
                        individual_vars.add(var)
        
        return {
            "individual_vars": list(individual_vars),
            "array_accesses": list(array_accesses),
            "main_expression": code.strip()
        }


class ResultExporter:
    """Handles saving analysis results to files."""

    @staticmethod
    def save_analysis_results(parser: PythonCodeParser, target_node: Node, 
                            path_analyzer: PathAnalyzer, symbolic_executor: SymbolicExecutor,
                            output_dir: str) -> str:
        """Orchestrates saving of all analysis data."""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Create Metadata Index
        index = {
            "metadata": {
                "generated_time": datetime.datetime.now().isoformat(),
                "version": "2.0.0",
                "target_node_line": target_node.line_number if target_node else None,
                "target_node_code": target_node.code if target_node else None,
            },
            "files": {}
        }
        
        # Save individual components
        ResultExporter._save_nodes_csv(parser, output_dir, index)
        ResultExporter._save_control_structures(parser, output_dir, index)
        
        if target_node:
            ResultExporter._save_target_node(target_node, output_dir, index)
            ResultExporter._save_path_analysis(path_analyzer, target_node, output_dir, index)
            ResultExporter._save_symbolic_analysis(symbolic_executor, target_node, output_dir, index)
            ResultExporter._save_variable_analysis(parser, target_node, output_dir, index)
            ResultExporter._save_report(parser, target_node, output_dir, index)
        
        # Save Index File
        index_path = os.path.join(output_dir, "index.json")
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(index, f, indent=2, ensure_ascii=False)
        
        return output_dir

    @staticmethod
    def _save_nodes_csv(parser: PythonCodeParser, output_dir: str, index: Dict):
        """Saves all parsed nodes to a CSV file."""
        csv_path = os.path.join(output_dir, "all_nodes.csv")
        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            # Standardized English Headers
            writer.writerow(["Line Number", "Code", "Node Type", "Condition", "Indent Level", "Is Actual Code"])
            
            for line_num, node in sorted(parser.node_map.items()):
                writer.writerow([
                    node.line_number, 
                    node.code, 
                    node.node_type,
                    node.condition or "", 
                    node.indent_level,
                    "Yes" if node.is_actual_code else "No"
                ])
        
        index["files"]["all_nodes"] = csv_path

    @staticmethod
    def _save_control_structures(parser: PythonCodeParser, output_dir: str, index: Dict):
        """Saves control structures to JSON."""
        json_path = os.path.join(output_dir, "control_structures.json")
        control_info = [
            {
                "line_number": node.line_number,
                "code": node.code,
                "node_type": node.node_type,
                "condition": node.condition or "",
                "indent_level": node.indent_level
            }
            for node in parser.control_structures
        ]
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(control_info, f, indent=2, ensure_ascii=False)
        
        index["files"]["control_structures"] = json_path

    @staticmethod
    def _save_target_node(target_node: Node, output_dir: str, index: Dict):
        """Saves details of the specific node under analysis."""
        json_path = os.path.join(output_dir, "target_node.json")
        node_info = {
            "line_number": target_node.line_number,
            "code": target_node.code,
            "node_type": target_node.node_type,
            "condition": target_node.condition,
            "indent_level": target_node.indent_level,
            "is_actual_code": target_node.is_actual_code
        }
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(node_info, f, indent=2, ensure_ascii=False)
        
        index["files"]["target_node"] = json_path

    @staticmethod
    def _save_path_analysis(path_analyzer: PathAnalyzer, target_node: Node, 
                          output_dir: str, index: Dict):
        """Saves the calculated execution paths."""
        path_info = path_analyzer.get_contextual_execution_path(target_node)
        
        serializable_info = {
            "main_path": [
                {
                    "line_number": info["node"].line_number,
                    "code": info["node"].code,
                    "node_type": info["node"].node_type,
                    "condition": info["node"].condition,
                    "context": info["context"]
                }
                for info in path_info["main_path"]
            ],
            "alternative_paths": [
                {
                    "description": alt["description"],
                    "path": [
                        {
                            "line_number": node.line_number,
                            "code": node.code,
                            "node_type": node.node_type,
                            "condition": node.condition
                        }
                        for node in alt["path"] if hasattr(node, "line_number")
                    ]
                }
                for alt in path_info["alternative_paths"]
            ]
        }
        
        json_path = os.path.join(output_dir, "path_analysis.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(serializable_info, f, indent=2, ensure_ascii=False)
        
        index["files"]["path_analysis"] = json_path

    @staticmethod
    def _save_symbolic_analysis(symbolic_executor: SymbolicExecutor, target_node: Node,
                              output_dir: str, index: Dict):
        """Saves symbolic execution results."""
        result = symbolic_executor.analyze_path(target_node)
        
        serializable_result = {
            "target_node": {
                "line_number": result["target_node"].line_number,
                "code": result["target_node"].code,
                "node_type": result["target_node"].node_type
            },
            "execution_path": [
                {
                    "line_number": node.line_number,
                    "code": node.code,
                    "node_type": node.node_type
                }
                for node in result["execution_path"]
            ],
            "path_constraints": [
                {
                    "node": {"line_number": node.line_number, "code": node.code},
                    "condition": condition,
                    "is_positive": is_positive
                }
                for node, condition, is_positive in result["path_constraints"]
            ],
            "combined_constraint": result["combined_constraint"]
        }
        
        json_path = os.path.join(output_dir, "symbolic_analysis.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(serializable_result, f, indent=2, ensure_ascii=False)
        
        index["files"]["symbolic_analysis"] = json_path

    @staticmethod
    def _save_variable_analysis(parser: PythonCodeParser, target_node: Node,
                              output_dir: str, index: Dict):
        """Saves variable extraction and reference results."""
        var_info = VariableAnalyzer.extract_variables_from_code(target_node.code)
        
        variable_references = {}
        all_vars = var_info['individual_vars'] + var_info['array_accesses']
        
        for var in all_vars:
            references = [
                {
                    "line_number": ref.line_number,
                    "code": ref.code,
                    "node_type": ref.node_type,
                    "is_modification": ("=" in ref.code and 
                                      not ref.code.strip().startswith(("if ", "while ", "for ")) and
                                      var in ref.code.split("=")[0])
                }
                for ref in parser.find_all_references(var)
                if ref.line_number < target_node.line_number
            ]
            
            variable_references[var] = sorted(references, key=lambda x: x["line_number"])
        
        analysis = {
            "extracted_info": var_info,
            "variable_references": variable_references
        }
        
        json_path = os.path.join(output_dir, "variable_analysis.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, indent=2, ensure_ascii=False)
        
        index["files"]["variable_analysis"] = json_path

    @staticmethod
    def _save_report(parser: PythonCodeParser, target_node: Node, 
                    output_dir: str, index: Dict):
        """Generates a human-readable text report."""
        report_path = os.path.join(output_dir, "analysis_report.txt")
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("===== Static Code Analysis Report =====\n\n")
            f.write(f"Generated at: {datetime.datetime.now().isoformat()}\n")
            f.write(f"Total LOC: {len(parser.node_map)}\n")
            f.write(f"Control Structures: {len(parser.control_structures)}\n\n")
            
            f.write(f"Target Node: Line {target_node.line_number}: {target_node.code}\n")
            f.write(f"Node Type: {target_node.node_type}\n")
            if target_node.condition:
                f.write(f"Condition: {target_node.condition}\n")
        
        index["files"]["analysis_report"] = report_path


class EnhancedPythonAnalyzer:
    """Wrapper class that integrates multiple analysis tools."""

    def __init__(self, code: str):
        self.parser = PythonCodeParser(code)
        self.path_analyzer = PathAnalyzer(self.parser)
        self.symbolic_executor = SymbolicExecutor(self.parser)

    def analyze_node(self, line_number: int) -> Optional[Dict[str, Any]]:
        """Analyzes a specific node by its line number."""
        target_node = self.parser.find_node_by_line(line_number)
        if not target_node:
            return None
        
        return {
            "target_node": target_node,
            "execution_path": self.parser.get_execution_path(target_node),
            "contextual_path": self.path_analyzer.get_contextual_execution_path(target_node),
            "symbolic_analysis": self.symbolic_executor.analyze_path(target_node),
            "variable_info": VariableAnalyzer.extract_variables_from_code(target_node.code)
        }

    def save_analysis(self, target_node: Node, output_dir: str) -> str:
        """Saves the analysis results to the specified directory."""
        return ResultExporter.save_analysis_results(
            self.parser, target_node, self.path_analyzer, 
            self.symbolic_executor, output_dir
        )

    def print_analysis(self, analysis_result: Dict[str, Any]):
        """Prints the analysis results to the console."""
        target_node = analysis_result["target_node"]
        print(f"\n===== Analyzing Node: Line {target_node.line_number} =====")
        print(f"Code: {target_node.code}")
        print(f"Type: {target_node.node_type}")
        if target_node.condition:
            print(f"Condition: {target_node.condition}")
        
        print("\nExecution Path:")
        for node in analysis_result["execution_path"]:
            print(f"  Line {node.line_number}: {node.code}")
        
        print("\nSymbolic Execution Constraints:")
        symbolic = analysis_result["symbolic_analysis"]
        for node, condition, is_positive in symbolic["path_constraints"]:
            constraint_type = "Satisfied" if is_positive else "Not Satisfied"
            print(f"  Line {node.line_number} ({constraint_type}): {condition}")
        
        print(f"\nCombined Constraint: {symbolic['combined_constraint']}")


def main():
    """Main entry point for the command line interface."""
    parser = argparse.ArgumentParser(description="Python Static Code Analysis Tool")
    parser.add_argument("file_path", help="Path to the Python file to analyze")
    parser.add_argument("--line_number", type=int, help="Line number of the specific node to analyze")
    parser.add_argument("--save_results", action="store_true", help="Flag to save analysis results to files")
    
    # Use a relative path by default, but handle it cleanly in logic
    default_output = os.path.join(".", "analysis_output")
    parser.add_argument("--output_dir", default=default_output, help="Directory to save output files")
    
    args = parser.parse_args()
    
    # Ensure file exists
    if not os.path.exists(args.file_path):
        print(f"Error: File not found at {args.file_path}")
        return

    # Read file
    with open(args.file_path, 'r', encoding='utf-8') as f:
        code = f.read()
    
    # Initialize Analyzer
    analyzer = EnhancedPythonAnalyzer(code)
    
    if args.line_number:
        # Analyze specific node
        result = analyzer.analyze_node(args.line_number)
        if result:
            analyzer.print_analysis(result)
            
            if args.save_results:
                output_dir = analyzer.save_analysis(result["target_node"], args.output_dir)
                print(f"\nAnalysis results saved to: {os.path.abspath(output_dir)}")
        else:
            print(f"No node found at line number {args.line_number}")
    else:
        # Print overall structure (assuming print_tree exists in the parser)
        print("Code Structure Tree:")
        analyzer.parser.print_tree()


if __name__ == "__main__":
    main()