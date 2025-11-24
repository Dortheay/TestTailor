import json
import csv
import os
import datetime
import argparse
from typing import List, Dict, Any, Tuple, Optional
from python_code_structure_parser import PythonCodeParser, Node

class PathAnalyzer:
    """Path Analyzer"""
    def __init__(self, parser: PythonCodeParser):
        self.parser = parser
    
    def get_contextual_execution_path(self, target_node: Node) -> Dict[str, Any]:
        """Get execution path with context information"""
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

        alternative_paths = self._generate_alternative_paths(main_path)
        
        return {
            "main_path": contextual_info,
            "alternative_paths": alternative_paths
        }
    
    def _generate_alternative_paths(self, main_path: List[Node]) -> List[Dict[str, Any]]:
        """Generate alternative execution paths"""
        alternative_paths = []
        
        for i, node in enumerate(main_path):
            if node.node_type in ['if', 'elif', 'else']:
                siblings = self.parser.get_siblings(node)
                condition_siblings = [s for s in siblings 
                                      if s.node_type in ['if', 'elif', 'else']]
                
                for sibling in condition_siblings:
                    alt_path = main_path[:i] + [sibling]
                    description = (f"Alternative path if '{sibling.condition or sibling.code}' "
                                   f"is taken instead of '{node.condition or node.code}'")
                    
                    alternative_paths.append({
                        "path": alt_path,
                        "description": description
                    })
        
        return alternative_paths

class SymbolicExecutor:
    """Symbolic Executor"""
    def __init__(self, parser: PythonCodeParser):
        self.parser = parser
    
    def get_path_constraints(self, target_node: Node) -> List[Tuple[Node, str, bool]]:
        """Get path constraints to reach the target node"""
        path = self.parser.get_execution_path(target_node)
        constraints = []
        
        for node in path:
            if node.node_type == 'if' and node.condition:
                constraints.append((node, node.condition, True))
            
            elif node.node_type in ['elif', 'else']:
                chain = self._get_if_elif_chain(node)
                
                for chain_node in chain:
                    if (chain_node.line_number < node.line_number and 
                        chain_node.condition):
                        negated = self._negate_condition(chain_node.condition)
                        constraints.append((chain_node, negated, False))
                
                if node.condition:
                    constraints.append((node, node.condition, True))
            
            elif node.node_type in ['while', 'for'] and node.condition:
                constraints.append((node, node.condition, True))
        
        return constraints
    
    def _get_if_elif_chain(self, node: Node) -> List[Node]:
        """Get if-elif-else chain"""
        siblings = self.parser.get_siblings(node)
        chain = [s for s in siblings if s.node_type in ('if', 'elif', 'else')]
        
        if node not in chain:
            chain.append(node)
        
        return sorted(chain, key=lambda n: n.line_number)
    
    def _negate_condition(self, condition: str) -> str:
        """Negate a condition"""
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
        """Combine all path constraints"""
        if not constraints:
            return "No constraints found."
        
        positive = [f"({cond})" for _, cond, is_pos in constraints if is_pos]
        negative = [f"not ({cond})" for _, cond, is_pos in constraints if not is_pos]
        
        parts = []
        if positive:
            parts.append(" and ".join(positive))
        if negative:
            parts.append(" and ".join(negative))
        
        return " and ".join(parts)
    
    def analyze_path(self, target_node: Node) -> Dict[str, Any]:
        """Analyze the complete path to the target node"""
        execution_path = self.parser.get_execution_path(target_node)
        path_constraints = self.get_path_constraints(target_node)
        
        return {
            "target_node": target_node,
            "execution_path": execution_path,
            "path_constraints": path_constraints,
            "combined_constraint": self._combine_constraints(path_constraints)
        }

class VariableAnalyzer:
    """Variable Analyzer"""
    @staticmethod
    def extract_variables_from_code(code: str) -> Dict[str, Any]:
        """Extract variable information from code"""
        import ast
        import re

        keywords = {
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
        
        individual_vars = set()
        array_accesses = set()
        
        try:
            tree = ast.parse(code.strip())
            
            class VariableVisitor(ast.NodeVisitor):
                def visit_Name(self, node):
                    if node.id not in keywords:
                        individual_vars.add(node.id)
                    self.generic_visit(node)
                
                def visit_Subscript(self, node):
                    if isinstance(node.value, ast.Name):
                        var_name = node.value.id
                        if var_name not in keywords:
                            individual_vars.add(var_name)
                            try:
                                full_access = ast.unparse(node)
                                array_accesses.add(full_access)
                            except:
                                array_accesses.add(f"{var_name}[...]")
                    elif isinstance(node.value, ast.Subscript):
                        try:
                            full_access = ast.unparse(node)
                            array_accesses.add(full_access)
                        except:
                            pass
                    
                    self.generic_visit(node)
                
                def visit_Attribute(self, node):
                    if isinstance(node.value, ast.Name):
                        var_name = node.value.id
                        if var_name not in keywords:
                            individual_vars.add(var_name)
                            try:
                                full_access = ast.unparse(node)
                                array_accesses.add(full_access)
                            except:
                                array_accesses.add(f"{var_name}.{node.attr}")
                    
                    self.generic_visit(node)
            
            visitor = VariableVisitor()
            visitor.visit(tree)
            
        except SyntaxError:
            print(f"AST parsing failed for: {code}, falling back to regex")

            code_clean = re.sub(r'#.*$', '', code, flags=re.MULTILINE)
            code_clean = re.sub(r'""".*?"""', '', code_clean, flags=re.DOTALL)  
            code_clean = re.sub(r"'''.*?'''", '', code_clean, flags=re.DOTALL)
            code_clean = re.sub(r'"(?:[^"\\]|\\.)*"', '', code_clean)  
            code_clean = re.sub(r"'(?:[^'\\]|\\.)*'", '', code_clean)  

            array_pattern = r'([a-zA-Z_][a-zA-Z0-9_]*(?:\[[^\]]+\])+)'
            array_matches = re.findall(array_pattern, code_clean)
            for match in array_matches:
                array_accesses.add(match)
                base_var = re.match(r'([a-zA-Z_][a-zA-Z0-9_]*)', match)
                if base_var:
                    individual_vars.add(base_var.group(1))

            attr_pattern = r'([a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)*)'
            attr_matches = re.findall(attr_pattern, code_clean)
            for match in attr_matches:
                array_accesses.add(match)
                base_var = match.split('.')[0]
                individual_vars.add(base_var)

            variable_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
            potential_vars = re.findall(variable_pattern, code_clean)
            
            for var in potential_vars:
                if var not in keywords:
                    func_call_pattern = rf'\b{re.escape(var)}\s*\('
                    if not re.search(func_call_pattern, code):
                        individual_vars.add(var)
        
        return {
            "individual_vars": list(individual_vars),
            "array_accesses": list(array_accesses),
            "main_expression": code.strip()
        }

class ResultExporter:
    """Result Exporter"""
    @staticmethod
    def save_analysis_results(parser: PythonCodeParser, target_node: Node, 
                              path_analyzer: PathAnalyzer, symbolic_executor: SymbolicExecutor,
                              output_dir: str) -> str:
        """Save all analysis results"""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        index = {
            "metadata": {
                "generated_time": datetime.datetime.now().isoformat(),
                "version": "2.0.0",
                "target_node_line": target_node.line_number if target_node else None,
                "target_node_code": target_node.code if target_node else None,
            },
            "files": {}
        }

        ResultExporter._save_nodes_csv(parser, output_dir, index)
        ResultExporter._save_control_structures(parser, output_dir, index)
        
        if target_node:
            ResultExporter._save_target_node(target_node, output_dir, index)
            ResultExporter._save_path_analysis(path_analyzer, target_node, output_dir, index)
            ResultExporter._save_symbolic_analysis(symbolic_executor, target_node, output_dir, index)
            ResultExporter._save_variable_analysis(parser, target_node, output_dir, index)
            ResultExporter._save_report(parser, target_node, output_dir, index)

        index_path = os.path.join(output_dir, "index.json")
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(index, f, indent=2, ensure_ascii=False)
        
        return output_dir

# ... rest of the methods (_save_nodes_csv, _save_control_structures, etc.) 
# can remain the same as long as CSV headers and report text are converted to English, 
# e.g., "Line Number", "Code", "Type", "Condition", "Indent Level", "Is Actual Code".

# In main() function, replace file_path help string:
# parser.add_argument("file_path", help="Path to the Python file to analyze")
# parser.add_argument("--output_dir", default="./analysis_output", help="Output directory path")
