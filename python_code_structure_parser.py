import ast
import re
from typing import List, Optional, Dict, Tuple


class Node:
    """Code node class"""
    def __init__(self, code: str, line_number: int, parent=None, indent_level: int = 0):
        self.code = code.rstrip()
        self.line_number = line_number
        self.parent = parent
        self.children = []
        self.indent_level = indent_level
        self.function_root = None
        self.included_lines = [line_number]  # record all included line numbers
        
        # additional attributes
        self.node_type = self._determine_node_type()
        self.condition = self._extract_condition()
        self.is_actual_code = True
        self.function_owner = None
    
    def add_child(self, child):
        """Add child node"""
        self.children.append(child)
        child.parent = self
        if self.function_root:
            child.function_root = self.function_root
    
    def _determine_node_type(self) -> str:
        """Determine node type"""
        code = self._clean_code()
        
        stripped_code = code.strip()
        if (stripped_code.startswith('"""') and stripped_code.endswith('"""')) or \
           (stripped_code.startswith("'''") and stripped_code.endswith("'''")):
            return 'comment'
        
        type_mapping = {
            'if ': 'if', 'elif ': 'elif', 'else': 'else',
            'for ': 'for', 'while ': 'while',
            'try': 'try', 'except ': 'except', 'finally': 'finally',
            'def ': 'function', 'class ': 'class',
            'return ': 'return', 'break': 'break', 'continue': 'continue'
        }
        
        for prefix, node_type in type_mapping.items():
            if code.startswith(prefix):
                return node_type
        
        return 'comment' if code.startswith('#') else 'statement'
    
    def _clean_code(self) -> str:
        """Clean code, remove comments"""
        code = self.code.strip()
        if '#' in code:
            in_quote = False
            quote_char = None
            for i, char in enumerate(code):
                if char in ['"', "'"] and (i == 0 or code[i-1] != '\\'):
                    if not in_quote:
                        in_quote = True
                        quote_char = char
                    elif char == quote_char:
                        in_quote = False
                elif char == '#' and not in_quote:
                    code = code[:i].strip()
                    break
        return code
    
    def _extract_condition(self) -> Optional[str]:
        """Extract condition expression"""
        code = self._clean_code()
        
        if self.node_type in ['if', 'elif', 'while']:
            try:
                if not code.endswith(':'):
                    code += ':'
                parsed = ast.parse(code)
                stmt = parsed.body[0]
                
                if isinstance(stmt, (ast.If, ast.While)):
                    return ast.unparse(stmt.test)
            except:
                pattern = f"^{self.node_type}\\s+(.*?)(?=:$|$)"
                match = re.search(pattern, code, re.DOTALL)
                if match:
                    return match.group(1).strip()
        
        elif self.node_type == 'for':
            parts = code.split(' in ', 1)
            if len(parts) > 1:
                target = parts[0].replace('for', '', 1).strip()
                iter_expr = parts[1].strip().rstrip(':')
                return f"iteration of {target} over {iter_expr}"
        
        elif self.node_type == 'else':
            return "else branch"
        
        return None
    
    def __str__(self):
        return f"Line {self.line_number}: {self.code}"
    
    def __repr__(self):
        return self.__str__()


class FunctionNode(Node):
    """Function node class"""
    def __init__(self, code: str, line_number: int, indent_level: int = 0):
        super().__init__(code, line_number, None, indent_level)
        self.function_root = self


class PythonCodeParser:
    """Python code structure parser"""
    
    def __init__(self, code: str):
        self.code = code
        self.node_map: Dict[int, Node] = {}
        self.function_nodes: List[FunctionNode] = []
        self.root: Optional[Node] = None
        self.control_structures: List[Node] = []
        
        self._parse()
        self._post_process()
    
    def _parse(self):
        """Parse code"""
        lines = self.code.strip().split('\n')
        if not lines:
            return
        
        function_boundaries = self._find_function_boundaries(lines)
        
        if not function_boundaries:
            self._parse_as_single_block(lines)
        else:
            for start_idx, end_idx in function_boundaries:
                self._parse_function(lines, start_idx, end_idx)
            
            if self.function_nodes:
                self.root = self.function_nodes[0]
    
    def _find_function_boundaries(self, lines: List[str]) -> List[Tuple[int, int]]:
        """Find function boundaries"""
        boundaries = []
        current_start = None
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith('def ') and not stripped.startswith('#'):
                if current_start is not None:
                    boundaries.append((current_start, i))
                current_start = i
        
        if current_start is not None:
            boundaries.append((current_start, len(lines)))
        
        return boundaries
    
    def _parse_as_single_block(self, lines: List[str]):
        """Parse as a single code block"""
        if not lines:
            return
        
        merged_lines = self._merge_continuation_lines(lines)
        if not merged_lines:
            return
        
        first_merged = merged_lines[0]
        self.root = Node(first_merged[0], first_merged[1])
        self.root.included_lines = first_merged[2]
        self.node_map[first_merged[1]] = self.root
        
        for line_num in first_merged[2]:
            self.node_map[line_num] = self.root
        
        stack = [(self.root, self._get_indent_level(first_merged[0]))]
        
        for merged_line, start_line_num, included_lines in merged_lines[1:]:
            if not merged_line.strip():
                continue
            
            indent_level = self._get_indent_level(merged_line)
            while stack and indent_level <= stack[-1][1]:
                stack.pop()
            
            parent = stack[-1][0] if stack else self.root
            new_node = Node(merged_line, start_line_num, parent, indent_level)
            new_node.included_lines = included_lines
            parent.add_child(new_node)
            
            for line_num in included_lines:
                self.node_map[line_num] = new_node
            
            stack.append((new_node, indent_level))

    def _parse_function(self, lines: List[str], start_idx: int, end_idx: int):
        """Parse a single function"""
        function_lines = lines[start_idx:end_idx]
        if not function_lines:
            return
        
        merged_lines = self._merge_continuation_lines(function_lines)
        if not merged_lines:
            return
        
        func_def_merged = merged_lines[0][0]
        func_def_included_lines = [start_idx + line_num - 1 for line_num in merged_lines[0][2]]
        
        func_node = FunctionNode(func_def_merged, start_idx + 1, self._get_indent_level(func_def_merged))
        func_node.included_lines = func_def_included_lines
        self.function_nodes.append(func_node)
        
        for line_num in func_def_included_lines:
            self.node_map[line_num + 1] = func_node
        
        base_indent = self._get_indent_level(func_def_merged)
        stack = [(func_node, base_indent)]
        
        for merged_line, relative_start, included_lines in merged_lines[1:]:
            if not merged_line.strip():
                continue
            
            indent_level = self._get_indent_level(merged_line)
            absolute_start = start_idx + relative_start
            absolute_included_lines = [start_idx + line_num for line_num in included_lines]
            
            while stack and indent_level <= stack[-1][1]:
                stack.pop()
            
            parent = stack[-1][0] if stack else func_node
            new_node = Node(merged_line, absolute_start, parent, indent_level)
            new_node.function_root = func_node
            new_node.included_lines = absolute_included_lines
            parent.add_child(new_node)
            
            for line_num in absolute_included_lines:
                self.node_map[line_num] = new_node
            
            stack.append((new_node, indent_level))
    
    def _get_indent_level(self, line: str) -> int:
        return len(line) - len(line.lstrip())
    
    def _is_continuation_line(self, line: str, prev_line: str) -> bool:
        line_stripped = line.strip()
        prev_stripped = prev_line.strip()
        
        if prev_stripped.endswith('\\'):
            return True
        
        open_brackets = prev_stripped.count('(') - prev_stripped.count(')')
        open_squares = prev_stripped.count('[') - prev_stripped.count(']')
        open_braces = prev_stripped.count('{') - prev_stripped.count('}')
        
        if open_brackets > 0 or open_squares > 0 or open_braces > 0:
            return True
        
        if prev_stripped.endswith(','):
            return True
        
        operators = ['and', 'or', 'not', '+', '-', '*', '/', '//', '%', '**', 
                     '==', '!=', '<', '>', '<=', '>=', 'is', 'in']
        if any(prev_stripped.endswith(' ' + op) for op in operators):
            return True
        
        if any(line_stripped.startswith(op + ' ') for op in ['and', 'or']):
            return True
        
        return False

    def _merge_continuation_lines(self, lines: List[str]) -> List[Tuple[str, int, List[int]]]:
        merged_lines = []
        i = 0
        
        while i < len(lines):
            current_line = lines[i]
            start_line_num = i + 1
            included_lines = [i + 1]
            
            if not current_line.strip():
                merged_lines.append((current_line, start_line_num, included_lines))
                i += 1
                continue
            
            j = i + 1
            while j < len(lines):
                if not lines[j].strip():
                    j += 1
                    continue
                    
                if self._is_continuation_line(lines[j], current_line):
                    current_line = current_line.rstrip() + ' ' + lines[j].strip()
                    included_lines.append(j + 1)
                    j += 1
                else:
                    break
            
            merged_lines.append((current_line, start_line_num, included_lines))
            i = j
        
        return merged_lines

    def _post_process(self):
        self._mark_actual_code()
        self._mark_function_boundaries()
        self._identify_control_structures()
    
    def _mark_actual_code(self):
        try:
            tree = ast.parse(self.code)
            docstring_lines = set()
            import_lines = set()
            
            for node in ast.walk(tree):
                if isinstance(node, (ast.Import, ast.ImportFrom)) and hasattr(node, 'lineno'):
                    import_lines.add(node.lineno)
            
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
                    if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant) and isinstance(node.body[0].value.value, str):
                        docstring_lines.add(node.body[0].lineno)
            
            if tree.body and isinstance(tree.body[0], ast.Expr) and isinstance(tree.body[0].value, ast.Constant) and isinstance(tree.body[0].value.value, str):
                docstring_lines.add(tree.body[0].lineno)
            
            for node in self.node_map.values():
                code = node.code.strip()
                node.is_actual_code = (
                    bool(code) and
                    not code.startswith('#') and
                    not (code.startswith("'''") and code.endswith("'''")) and
                    not (code.startswith('"""') and code.endswith('"""')) and
                    node.line_number not in docstring_lines and
                    node.line_number not in import_lines
                )
        
        except SyntaxError:
            for node in self.node_map.values():
                code = node.code.strip()
                node.is_actual_code = (
                    bool(code) and
                    not code.startswith('#') and
                    not code.startswith(('import ', 'from '))
                )

    def _mark_function_boundaries(self):
        function_ranges = []
        
        for func_node in self.function_nodes:
            start_line = func_node.line_number
            end_line = float('inf')
            
            for node in sorted(self.node_map.values(), key=lambda n: n.line_number):
                if node.line_number > start_line and node.indent_level <= func_node.indent_level:
                    end_line = node.line_number - 1
                    break
            
            function_ranges.append({
                'function_node': func_node,
                'start_line': start_line,
                'end_line': end_line
            })
        
        for node in self.node_map.values():
            node.function_owner = None
            for func_range in function_ranges:
                if func_range['start_line'] <= node.line_number <= func_range['end_line']:
                    node.function_owner = func_range['function_node']
                    break
    
    def _identify_control_structures(self):
        self.control_structures = [
            node for node in self.node_map.values()
            if node.node_type in ['if', 'elif', 'else', 'for', 'while', 'try', 'except', 'finally']
        ]
    
    def find_node_by_line(self, line_number: int) -> Optional[Node]:
        return self.node_map.get(line_number)
    
    def find_node_by_code(self, code_snippet: str, partial_match: bool = True) -> Optional[Node]:
        code_snippet = code_snippet.strip()
        for node in self.node_map.values():
            if partial_match:
                if code_snippet in node.code:
                    return node
            else:
                if code_snippet == node.code.strip():
                    return node
        return None
    
    def get_execution_path(self, node: Node) -> List[Node]:
        if not node:
            return []
        
        path = []
        current = node
        while current:
            path.insert(0, current)
            current = current.parent
        
        return [n for n in path if n.is_actual_code]
    
    def get_siblings(self, node: Node) -> List[Node]:
        if not node or not node.parent:
            return []
        return [child for child in node.parent.children if child != node and child.function_owner == node.function_owner]
    
    def find_all_references(self, variable_name: str) -> List[Node]:
        return [node for node in self.node_map.values() if variable_name in node.code and not node.code.strip().startswith('#') and node.is_actual_code]
    
    def print_tree(self, node: Optional[Node] = None, depth: int = 0):
        if node is None:
            node = self.root
        if not node:
            return
        
        print('  ' * depth + str(node))
        for child in node.children:
            self.print_tree(child, depth + 1)

    def find_parent_function(self, node: Node) -> Optional[Node]:
        """Find the function node containing the target node"""
        if not node:
            return None
        return node.function_owner
