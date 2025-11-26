"""
LLM Test Generator
==================

A tool to automatically generate Python unit tests using Large Language Models (LLMs).
It analyzes code structure, coverage, and existing test patterns to generate
high-quality test cases.

Dependencies:
    - openai
    - coverage
    - project_class_indexer (Local)
    - ImportGenerator (Local)
"""

import ast
import importlib
import importlib.util
import inspect
import json
import logging
import os
import re
import sys
import tempfile
import textwrap
import time
import traceback
import argparse
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Any
from contextlib import redirect_stdout, redirect_stderr

import coverage
import openai
import timeout_decorator

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("llm_test_gen.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Local imports (Assumed to be in the python path)
try:
    from project_class_indexer import ProjectClassIndexer
except ImportError:
    logger.warning("Could not import ProjectClassIndexer. Some features may be limited.")
    ProjectClassIndexer = None


class LLMTestGenerator:
    """
    Generates unit tests for a specific Python module using an LLM.
    """

    def __init__(
        self,
        api_key: str,
        target_module_path: str,
        model_name: str = "gpt-4o-2024-11-20",
        max_retries: int = 2,
        temperature: float = 1.0,
        api_base: str = "https://api.openai.com/v1"
    ):
        """
        Initialize the LLM Test Generator.

        Args:
            api_key: OpenAI API key.
            target_module_path: Path to the python file to be tested.
            model_name: The LLM model identifier.
            max_retries: Maximum number of retries for failed generations.
            temperature: Sampling temperature for the LLM.
            api_base: Base URL for the LLM API.
        """
        self.api_key = api_key
        self.model_name = model_name
        self.target_module_path = os.path.abspath(target_module_path)
        self.max_retries = max_retries
        self.temperature = temperature
        self.api_base = api_base

        if not os.path.exists(self.target_module_path):
            raise FileNotFoundError(f"Target module not found: {self.target_module_path}")

        # Load module content
        with open(self.target_module_path, 'r', encoding='utf-8') as f:
            self.module_code = f.read()

        # Metadata
        self.module_name = os.path.basename(self.target_module_path).replace('.py', '')
        self.module_dir = os.path.dirname(self.target_module_path)

        # Initialize coverage tool
        self.cov = coverage.Coverage(source=[self.target_module_path])

        # State tracking
        self.successful_tests = []
        self.messages = []
        self.llm_total_call_count = 0
        self.coverage_trace_log_path = os.path.join(self.module_dir, "llm_coverage_trace.jsonl")

        # Initialize Indexer
        if ProjectClassIndexer:
            self.project_indexer = ProjectClassIndexer(self.module_dir)
        else:
            self.project_indexer = None

    def _update_messages(self, prompt: str, role: str = "user", clear_history: bool = False):
        """
        Update the conversation history for the LLM.

        Args:
            prompt: The content string to add.
            role: The role of the message sender ("system", "user", "assistant").
            clear_history: If True, resets the conversation.
        """
        if clear_history:
            self.messages = []

        # Ensure system prompt exists
        if not self.messages or not any(msg["role"] == "system" for msg in self.messages):
            self.messages.append({
                "role": "system",
                "content": "You are a professional Python test engineer, skilled in writing high-quality test cases."
            })

        self.messages.append({
            "role": role,
            "content": prompt
        })

    def _get_current_coverage(self, test_dir: str) -> Tuple[float, Dict]:
        """
        Execute existing tests in `test_dir` and calculate coverage for the target module.

        Args:
            test_dir: Directory containing test files.

        Returns:
            Tuple containing (coverage_percentage, coverage_details_dict).
        """
        import unittest
        
        logger.info(f"Calculating coverage using tests in: {os.path.basename(test_dir)}")

        if not os.path.exists(test_dir):
            logger.error(f"Test directory does not exist: {test_dir}")
            return 0.0, {'error': 'Test directory does not exist'}

        # Discover tests
        test_files = [f for f in os.listdir(test_dir) if f.startswith('test_') and f.endswith('.py')]
        if not test_files:
            logger.warning("No test files found in the test directory.")
        else:
            logger.info(f"Found {len(test_files)} test files.")

        try:
            source_dir = os.path.dirname(self.target_module_path)
            data_file = os.path.join(self.module_dir, ".coverage")
            
            omit_patterns = ["*/tmp*.py", "*/__pycache__/*", "*/template*"]

            self.cov = coverage.Coverage(
                source=[source_dir],
                data_file=data_file,
                omit=omit_patterns
            )

            self.cov.start()
            
            # Run tests silently
            try:
                suite = unittest.defaultTestLoader.discover(test_dir)
                test_count = sum(test_case.countTestCases() for test_suite in suite for test_case in test_suite)
                logger.info(f"Executing {test_count} test cases...")

                with io.StringIO() as buffer:
                    with redirect_stdout(buffer):
                        runner = unittest.TextTestRunner(stream=buffer, verbosity=0)
                        result = runner.run(suite)

                if result.errors or result.failures:
                    logger.warning(f"Tests execution had issues: {len(result.errors)} errors, {len(result.failures)} failures.")
            
            except Exception as e:
                logger.error(f"Error executing tests: {str(e)}")

            self.cov.stop()
            self.cov.save()

            # Analyze data
            data = self.cov.get_data()
            measured_files = list(data.measured_files())
            
            total_lines, covered_lines = 0, 0
            coverage_by_file = {}
            target_basename = os.path.basename(self.target_module_path)

            for file in measured_files:
                if os.path.basename(file) == target_basename:
                    try:
                        _, executable, missing, _ = self.cov.analysis(file)
                        executed = list(set(executable) - set(missing))
                        
                        total_lines += len(executable)
                        covered_lines += len(executed)
                        
                        file_coverage = len(executed) / len(executable) if executable else 0
                        coverage_by_file[file] = {
                            'executable_lines': executable,
                            'executed_lines': executed,
                            'missing_lines': missing,
                            'coverage': file_coverage
                        }
                    except Exception as e:
                        logger.error(f"Error analyzing file coverage {file}: {e}")

            pct = (covered_lines / total_lines * 100.0) if total_lines > 0 else 0.0
            logger.info(f"Current coverage: {pct:.2f}% ({covered_lines}/{total_lines} lines)")

            return pct, {
                'total_lines': total_lines,
                'covered_lines': covered_lines,
                'coverage_by_file': coverage_by_file
            }

        except Exception as e:
            logger.error(f"Critical error in coverage calculation: {e}")
            return 0.0, {'error': str(e)}

    def _build_initial_prompt(self, group: Dict, project_dir: str, test_dir: str) -> str:
        """Construct the initial prompt for the LLM."""
        line_numbers = group.get('line_numbers', [])
        path_constraints = group.get("path_constraint", "")
        function_info = group.get('function_info', "")
        similarity_result = group.get('similarity_result', {})

        if not line_numbers:
             logger.warning("No line numbers provided for prompt generation.")
             return ""

        code_context = self.extract_context_by_line(line_numbers[0])

        prompt_sections = [
            self._build_function_under_test_section(code_context, line_numbers),
            self._build_path_constraint_section(path_constraints),
            self._build_similar_test_case_section(similarity_result, project_dir),
            self._build_task_instruction_section(function_info, test_dir)
        ]

        return '\n'.join(filter(None, prompt_sections))

    def _build_function_under_test_section(self, code_context: dict, line_numbers: list) -> str:
        sections = []
        start_line, end_line = line_numbers[0], line_numbers[-1]

        if code_context.get('class_info') and code_context.get('function_info'):
            sections.append("## Function under Test (with class context)")
            sections.append("```python")
            sections.append(code_context['class_info']['complete_info'])
            sections.append(code_context['function_info']['code'])
            sections.append("```")
        elif code_context.get('function_info'):
            sections.append("## Function under Test")
            sections.append("```python")
            sections.append(code_context['function_info']['code'])
            sections.append("```")

        sections.append("## Target Code Block to Cover")
        sections.append("```python")
        sections.append(self._get_code_segment(start_line, end_line))
        sections.append("```")

        if code_context.get("related_project_classes"):
            sections.append("## Related Classes")
            for cls in code_context["related_project_classes"]:
                if cls.get("file"):
                    sections.append(f"Source File: {cls['file']}\n")
                if cls.get("init_method"):
                    sections.append("Class Definition:\n```python")
                    sections.append(cls["init_method"])
                    sections.append("```")

        return '\n'.join(sections)

    def _build_path_constraint_section(self, path_constraints: str) -> str:
        if not path_constraints:
            return ""
        return f"""
## Execution Path Constraints
To reach the target code, the test case must satisfy the following conditions:
```python
{path_constraints}
```
"""

    def _build_similar_test_case_section(self, similarity_result: dict, project_dir: str) -> str:
        best_test_case = similarity_result.get('best_test_case')
        if not best_test_case:
            return ""

        try:
            test_case_code = self._get_test_case_code(best_test_case, Path(project_dir))
        except Exception as e:
            logger.warning(f"Failed to retrieve similar test case code: {e}")
            return ""

        sections = [
            "## Reference: Most Path-Similar Test Case",
            "```python",
            test_case_code,
            "```"
        ]

        divergence = similarity_result.get('path_divergence', {})
        if divergence.get('has_divergence'):
            dp = divergence.get('divergence_point', {})
            div_line = dp.get('line', '')
            
            if div_line:
                div_code = self._get_code_segment(div_line, div_line)
                sections.append(f"\n## Path Divergence Analysis\nThe reference test diverges at line {div_line}: `{div_code.strip()}`")

            # Add context about where paths go
            for kind, label in [('next_static', "Target path continues to"), ('next_dynamic', "Reference path continues to")]:
                next_node = dp.get(kind)
                if next_node and len(next_node) >= 2:
                    line = next_node[1]
                    code = self._get_code_segment(line, line).strip() or str(line)
                    sections.append(f"{label}: Line {line} -> `{code}`")

            # Variable state at divergence
            var_state = divergence.get('variable_state', {})
            if var_state and div_line:
                div_code = self._get_code_segment(div_line, div_line)
                important_vars = self._extract_code_variables(div_code, var_state)
                if important_vars:
                    sections.append(f"\nAt the divergence point, the reference test has these variable states:\n{self._format_variable_state(important_vars)}")

        return '\n'.join(sections)

    def _build_task_instruction_section(self, function_info: str, test_dir: str) -> str:
        # Dynamic import of helper to avoid circular dependency at top level if not strictly needed
        try:
            from ImportGenerator import ImportGenerator
            import_gen = ImportGenerator(test_dir)
            imports = '\n'.join(import_gen.process_test_files())
        except ImportError:
            logger.warning("ImportGenerator not found. Using default imports.")
            imports = "import unittest\nimport timeout_decorator"

        if "import unittest" not in imports:
            imports += "\nimport unittest"
        if "import timeout_decorator" not in imports:
            imports += "\nimport timeout_decorator"

        return f'''
## Task
Create a new test case that covers the target code branch. Use the reference test case as a guide but modify the logic to satisfy the path constraints.

## Requirements:

Return ONLY the python code for the test class.

Do not include import statements (they are pre-provided).

Start from the class Test(unittest.TestCase): line.

## Pre-defined Imports:

{imports}

class Test(unittest.TestCase):
    @timeout_decorator.timeout(1)
    def test_case_{function_info}(self):
        """Implement test case here"""
```
'''

    def _call_llm(self) -> Dict[str, Any]:
        """Call the OpenAI API."""
        try:
            if not self.messages:
                raise ValueError("Message history is empty.")
            
            client = openai.OpenAI(api_key=self.api_key, base_url=self.api_base)
            
            response = client.chat.completions.create(
                model=self.model_name,
                messages=self.messages,
                temperature=self.temperature,
                max_tokens=4000
            )
            
            self.llm_total_call_count += 1
            content = ""
            if response.choices:
                content = response.choices[0].message.content
            
            usage_info = {}
            if response.usage:
                usage_info = {
                    'prompt_tokens': response.usage.prompt_tokens,
                    'completion_tokens': response.usage.completion_tokens,
                    'total_tokens': response.usage.total_tokens
                }

            finish_reason = response.choices[0].finish_reason if response.choices else None
            
            # Add assistant response to history
            self._update_messages(content, "assistant", False)
            
            return {
                'content': content,
                'usage': usage_info,
                'finish_reason': finish_reason,
            }
        except Exception as e:
            logger.error(f"LLM API Call Failed: {e}")
            return {'content': '', 'usage': {}, 'finish_reason': 'error'}

    def _extract_code_variables(self, code_line: str, variable_state: Dict) -> Dict:
        """Extract relevant variable values for a specific line of code."""
        if not code_line or not variable_state:
            return {}
        
        locals_vars = variable_state.get('locals', {})
        if not locals_vars:
            return {}
        
        potential_vars = set(re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', code_line))
        
        keywords = {
            'if', 'else', 'elif', 'for', 'while', 'try', 'except', 'with', 'return', 
            'and', 'or', 'not', 'in', 'is', 'True', 'False', 'None', 'class', 'def',
            'import', 'from', 'as', 'pass', 'break', 'continue', 'print', 'len',
            'str', 'int', 'float', 'list', 'dict', 'set', 'tuple'
        }
        
        relevant_vars = {}
        for var_name in potential_vars:
            if var_name in locals_vars and var_name not in keywords:
                var_value = locals_vars[var_name]
                
                # Simplify complex objects for display
                if var_name in ['node', 'body'] and isinstance(var_value, dict) and 'class' in var_value:
                    relevant_vars[var_name] = f"AST Node ({var_value.get('class')})"
                elif isinstance(var_value, dict) and len(var_value) > 3:
                    keys = list(var_value.keys())[:3]
                    relevant_vars[var_name] = f"dict(len={len(var_value)}, keys={keys}...)"
                elif isinstance(var_value, (list, tuple)) and len(var_value) > 3:
                    relevant_vars[var_name] = f"{type(var_value).__name__}(len={len(var_value)})"
                elif isinstance(var_value, str) and len(var_value) > 100:
                    relevant_vars[var_name] = f"{var_value[:50]}... (len={len(var_value)})"
                else:
                    relevant_vars[var_name] = var_value
        
        return relevant_vars

    def _extract_test_code(self, llm_response: str) -> str:
        """Extract Python code block from Markdown response."""
        if not llm_response or not isinstance(llm_response, str):
            return ""
        match = re.search(r'```python(.*)```', llm_response, re.DOTALL)
        return match.group(1).strip() if match else ""

    def _generate_error_fix_prompt(self, test_code: str, error_message: str, test_dir: str) -> str:
        """Generate a prompt to fix a failing test."""
        prompt = f'''
The test case generated before didn't execute successfully. Here is the original test code:

```python
{test_code}
```
The error message is as follows:
{error_message}
Please fix the errors in the test case. Analyze what went wrong and make the necessary corrections.
** Important: Only provide the completed test case starting from "class Test" line. Do not include import statements. **

'''

    def generate_tests(self, group: Dict, project_dir: str, test_dir: str, new_test_dir: str, num_attempts: int = 3) -> Dict: 
        """ Main loop to generate, verify, and fix test cases.
                Args:
            group: Data structure containing target lines and context.
            project_dir: Root directory of the project.
            test_dir: Directory containing existing tests.
            new_test_dir: Directory to save generated tests.
            num_attempts: Max retry attempts.

        Returns:
            Dictionary containing generation report and results.
        """
        generation_record = {
            "timestamp": datetime.now().isoformat(),
            "target_module": self.target_module_path,
            "target_lines": group.get('line_numbers', []),
            "attempts": [],
            "total_usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
            "final_result": {"success": False}
        }

        # 1. Establish Baseline Coverage
        logger.info("Establishing baseline coverage...")
        _, cov_detail = self._get_current_coverage(str(new_test_dir))
        previously_covered = set()
        for f in cov_detail.get("coverage_by_file", {}).values():
            previously_covered.update(f.get("executed_lines", []))

        # 2. Initial Generation
        logger.info("Building initial prompt...")
        initial_prompt = self._build_initial_prompt(group, project_dir, test_dir)
        self._update_messages(initial_prompt, "user", clear_history=True)
        response = self._call_llm()

        # Update Usage Stats
        if response.get('usage'):
            for key in generation_record["total_usage"]:
                generation_record["total_usage"][key] += response['usage'].get(key, 0)

        test_code = self._extract_test_code(response['content'])
        test_result = self.run_test_case(test_code, project_dir, test_dir)

        result_lines = set(test_result.get('coverage', {}).get('covered_lines', []))
        newly_covered = result_lines - previously_covered

        attempt_record = {
            "attempt_number": 1,
            "type": "initial",
            "success": test_result['success'],
            "new_coverage": bool(newly_covered),
            "output": test_result.get('output', '')
        }
        generation_record["attempts"].append(attempt_record)

        # 3. Validation & Retry Loop
        current_code = test_code
        current_result = test_result
        success = False

        # Check initial result
        if current_result['success'] and newly_covered:
            success = True

        # Retry Loop
        attempt_count = 1
        while not success and attempt_count < num_attempts:
            logger.info(f"Attempt {attempt_count + 1}/{num_attempts}: "
                        f"{'Fixing Error' if not current_result['success'] else 'Improving Coverage'}...")

            if current_result['success']:
                # Ran but didn't cover target
                self._update_messages(initial_prompt, "user", True) # Should ideally be a specific refinement prompt
            else:
                # Execution failed
                self._generate_error_fix_prompt(current_code, current_result['output'], test_dir)

            response = self._call_llm()

            # Update Usage
            if response.get('usage'):
                for key in generation_record["total_usage"]:
                    generation_record["total_usage"][key] += response['usage'].get(key, 0)

            current_code = self._extract_test_code(response['content'])
            current_result = self.run_test_case(current_code, project_dir, test_dir)

            result_lines = set(current_result.get('coverage', {}).get('covered_lines', []))
            newly_covered = result_lines - previously_covered

            attempt_count += 1
            generation_record["attempts"].append({
                "attempt_number": attempt_count,
                "type": "retry",
                "success": current_result['success'],
                "new_coverage": bool(newly_covered)
            })

            if current_result['success'] and newly_covered:
                success = True

        # 4. Finalize
        if success:
            logger.info(f"✅ Success! Target lines covered: {group['line_numbers']}")
            os.makedirs(new_test_dir, exist_ok=True)

            first_line = group["line_numbers"][0] if group["line_numbers"] else 0
            filename = f"test_{self.module_name}_line{first_line}.py"
            filepath = os.path.join(new_test_dir, filename)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(current_result['test case'])

            generation_record["final_result"] = {
                "success": True,
                "file": filepath,
                "covered_lines": list(result_lines)
            }
            self.successful_tests.append(current_result['test case'])

            # Log coverage trace
            overall_pct, _ = self._get_current_coverage(str(new_test_dir))
            with open(self.coverage_trace_log_path, 'a', encoding='utf-8') as f:
                json_line = json.dumps({
                    "timestamp": datetime.now().isoformat(),
                    "module": self.target_module_path,
                    "coverage_pct": round(overall_pct, 2)
                })
                f.write(json_line + '\n')
        else:
            logger.warning("❌ Failed to generate valid test case after all attempts.")

        return generation_record

    def save_successful_tests(self, output_path: Optional[str] = None) -> None:
            """
            Save all successfully generated test cases to a single file.

            Args:
                output_path: The path to save the test file. If None, generates a default name.
            """
            if not self.successful_tests:
                logger.info("No successful test cases to save.")
                return

            if output_path is None:
                output_path = f"generated_tests_{self.module_name}.py"

            try:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write("# Automatically generated test cases\n")
                    f.write(f"import pytest\nfrom {self.module_name} import *\n\n")

                    for i, test in enumerate(self.successful_tests):
                        f.write(f"# Test Case {i + 1}\n")
                        # Remove redundant imports inside the snippet to keep the file clean
                        cleaned_test = re.sub(r'import pytest.*?\n', '', test)
                        cleaned_test = re.sub(r'from.*?import.*?\n', '', cleaned_test)
                        f.write(cleaned_test)
                        f.write("\n\n")

                logger.info(f"Successfully saved {len(self.successful_tests)} test cases to {output_path}")
            except IOError as e:
                logger.error(f"Failed to save test cases to {output_path}: {e}")


    def parse_line_numbers_from_similarity_json(json_path: str, target_filename: str) -> List[List[int]]:
        """
        Parse the similarity analysis JSON to extract line number groups for the target file.

        Args:
            json_path: Path to the 'similarity_analysis.json' file.
            target_filename: The name of the file being tested (e.g., 'utils.py').

        Returns:
            A list of lists, where each inner list contains line numbers (integers).
        """
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"JSON file not found: {json_path}")

        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            suggestions = data.get('suggestions_analysis', {})
            return suggestions.get(target_filename, [])
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON file {json_path}: {e}")
            return []

    def build_code_structure(self) -> Dict[str, Any]:
        """
        Parse the entire module code to build a structural map of classes and functions.
        
        Returns:
            A dictionary containing:
            - classes: List of class metadata.
            - functions: List of standalone function metadata.
            - line_to_context: Map of line numbers to their enclosing context.
        """
        try:
            tree = ast.parse(self.module_code)
        except SyntaxError as e:
            logger.error(f"Syntax error parsing module code: {e}")
            return {
                "classes": [],
                "functions": [],
                "line_to_context": {}
            }

        structure = {
            "classes": [],
            "functions": [],
            "line_to_context": {}  # line number -> {function, class}
        }

        # First pass: Identify classes and standalone functions
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                self._process_class_node(node, structure)
            elif isinstance(node, ast.FunctionDef):
                # Check if this function is already captured as a method of a class
                is_method = any(
                    cls["start_line"] <= node.lineno <= cls["end_line"]
                    for cls in structure["classes"]
                )
                if not is_method:
                    self._process_function_node(node, structure)

        # Second pass: Extract non-docstring comments
        self._extract_comments(structure)

        return structure

    def _process_class_node(self, node: ast.ClassDef, structure: Dict[str, Any]) -> None:
        """Helper to process AST ClassDef nodes."""
        end_line = getattr(node, 'end_lineno', node.lineno)
        
        methods = []
        init_method = None

        for child in node.body:
            if isinstance(child, ast.FunctionDef):
                method_info = self._extract_function_metadata(child)
                methods.append(method_info)
                if child.name == "__init__":
                    init_method = method_info

        class_info = {
            "name": node.name,
            "start_line": node.lineno,
            "end_line": end_line,
            "methods": methods,
            "init_method": init_method,
            "decorators": [self._get_decorator_name(d) for d in node.decorator_list],
            "docstring": ast.get_docstring(node),
            "header_comments": []
        }

        structure["classes"].append(class_info)

        # Map class lines to context
        for line in range(node.lineno, end_line + 1):
            structure["line_to_context"][line] = {
                "class": class_info,
                "function": None
            }

        # Map method lines to context (overwriting class context where appropriate)
        for method in methods:
            for line in range(method["actual_start_line"], method["end_line"] + 1):
                structure["line_to_context"][line] = {
                    "class": class_info,
                    "function": method
                }

    def _process_function_node(self, node: ast.FunctionDef, structure: Dict[str, Any]) -> None:
        """Helper to process standalone AST FunctionDef nodes."""
        func_info = self._extract_function_metadata(node)
        func_info["class"] = None  # Standalone function
        
        structure["functions"].append(func_info)

        for line in range(func_info["actual_start_line"], func_info["end_line"] + 1):
            structure["line_to_context"][line] = {
                "class": None,
                "function": func_info
            }

    def _extract_function_metadata(self, node: ast.FunctionDef) -> Dict[str, Any]:
        """Extract metadata from a FunctionDef node."""
        # Calculate actual start line including decorators
        actual_start_line = node.lineno
        if node.decorator_list and hasattr(node.decorator_list[0], 'lineno'):
            actual_start_line = node.decorator_list[0].lineno

        return {
            "name": node.name,
            "start_line": node.lineno,
            "actual_start_line": actual_start_line,
            "end_line": getattr(node, 'end_lineno', node.lineno),
            "params": [arg.arg for arg in node.args.args],
            "decorators": [self._get_decorator_name(d) for d in node.decorator_list],
            "docstring": ast.get_docstring(node),
            "header_comments": []
        }

    def _get_decorator_name(self, node: ast.AST) -> str:
        """Recursively resolve the name of a decorator."""
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Call):
            # Handle @decorator(args)
            return f"{self._get_decorator_name(node.func)}(...)"
        elif isinstance(node, ast.Attribute):
            # Handle @module.decorator
            return f"{self._get_decorator_name(node.value)}.{node.attr}"
        return "unknown"

    def _extract_comments(self, structure: Dict[str, Any]) -> None:
        """Extract header comments for classes and functions (excluding docstrings)."""
        lines = self.module_code.split('\n')

        def get_comments(start_line: int, end_line: int, docstring: Optional[str]) -> List[str]:
            comments = []
            current_line = start_line
            
            # Skip docstring lines approximation
            if docstring:
                current_line += docstring.count('\n') + 2
            
            # Scan following lines
            while current_line < len(lines) and current_line < end_line:
                line_content = lines[current_line - 1].strip()
                if not line_content or (line_content and not line_content.startswith('#')):
                    break
                comments.append(line_content)
                current_line += 1
            return comments

        for cls in structure["classes"]:
            cls["header_comments"] = get_comments(cls["start_line"], cls["end_line"], cls["docstring"])
            for method in cls["methods"]:
                method["header_comments"] = get_comments(method["start_line"], method["end_line"], method["docstring"])

        for func in structure["functions"]:
            func["header_comments"] = get_comments(func["start_line"], func["end_line"], func["docstring"])

    def _extract_used_classes(self, function_code: str) -> set:
        """Extract class names used within a function's source code."""
        used_classes = set()
        try:
            dedented_code = textwrap.dedent(function_code)
            tree = ast.parse(dedented_code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                    used_classes.add(node.func.id)
                elif isinstance(node, ast.Name):
                    used_classes.add(node.id)
                elif isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
                    used_classes.add(node.value.id)
        except Exception as e:
            logger.debug(f"AST parsing for used classes failed (this is expected for fragments): {e}")
        return used_classes

    def extract_context_by_line(self, line_number: int) -> Dict[str, Any]:
        """
        Retrieve code context (class/function info) for a specific line number.

        Args:
            line_number: The line number to query.

        Returns:
            Dict containing 'function_info', 'class_info', and 'related_project_classes'.
        """
        if not hasattr(self, '_code_structure'):
            self._code_structure = self.build_code_structure()

        context = self._code_structure["line_to_context"].get(line_number, {"class": None, "function": None})
        result = {
            "function_info": None,
            "class_info": None,
            "related_project_classes": []
        }

        # Process Function Info
        if context["function"]:
            func = context["function"]
            full_code = self._get_code_segment(func["actual_start_line"], func["end_line"])
            
            # Generate numbered code for better LLM comprehension
            func_lines = full_code.split('\n')
            numbered_code = '\n'.join(f"{func['actual_start_line'] + i}: {line}" 
                                      for i, line in enumerate(func_lines))

            result["function_info"] = {
                "name": func["name"],
                "params": ", ".join(func["params"]),
                "line_number": func["start_line"],
                "decorators": func.get("decorators", []),
                "docstring": func.get("docstring"),
                "code": full_code,
                "numbered_code": numbered_code
            }

            # Extract related class info if indexer is available
            if self.project_indexer:
                used_classes = self._extract_used_classes(full_code)
                for cls_name in used_classes:
                    cls_info = self.project_indexer.get_class_info(cls_name)
                    if cls_info:
                        result["related_project_classes"].append(cls_info)

        # Process Class Info
        if context["class"]:
            cls_info = context["class"]
            
            # Reconstruct class signature
            class_lines = []
            for dec in cls_info.get("decorators", []):
                class_lines.append(f"@{dec}")
            class_lines.append(f"class {cls_info['name']}:")
            
            if cls_info.get("docstring"):
                class_lines.append(f'    """{cls_info["docstring"]}"""')
            
            class_def_text = '\n'.join(class_lines)
            
            # Add __init__ code if available
            init_info = None
            if cls_info["init_method"]:
                init = cls_info["init_method"]
                init_code = self._get_code_segment(init["actual_start_line"], init["end_line"])
                class_def_text += f"\n\n{init_code}" # Append init code to class context

            result["class_info"] = {
                "name": cls_info["name"],
                "complete_info": class_def_text,
                "init_method": init_info
            }

        return result

    def _get_code_segment(self, start_line: int, end_line: int) -> str:
        """Extract a specific range of lines from the module code."""
        lines = self.module_code.split('\n')
        
        # Adjust for 0-based indexing vs 1-based line numbers
        start_idx = max(0, start_line - 1)
        end_idx = min(len(lines), end_line)
        
        if start_idx < len(lines):
            return '\n'.join(lines[start_idx:end_idx])
        return ""

    def _get_test_case_code(self, test_case: Dict, project_dir: Path) -> str:
        """
        Retrieve source code for a specific test case from the project files.
        """
        module_name = test_case.get('module', '')
        module_path = project_dir / f"{module_name.replace('.', '/')}.py"
        
        project_str = str(project_dir)
        sys_path_modified = False

        if project_str not in sys.path:
            sys.path.insert(0, project_str)
            sys_path_modified = True

        try:
            # Calculate relative import path
            rel_path = module_path.relative_to(project_dir)
            import_path = str(rel_path.with_suffix('')).replace(os.sep, '.')
            
            module = importlib.import_module(import_path)
            module_source = inspect.getsource(module)
            imports = self._extract_imports(module_source)

            # Extract target class or method
            if test_case.get('class'):
                target_cls = getattr(module, test_case['class'])
                target_source = inspect.getsource(target_cls)
                full_code = f"{imports}\n\n{target_source}"
            else:
                target_func = getattr(module, test_case['method'])
                target_source = inspect.getsource(target_func)
                full_code = f"{imports}\n\n{target_source}"

            return full_code
        except Exception as e:
            logger.error(f"Error retrieving test case code: {e}")
            raise RuntimeError(f"Could not load test case: {e}")
        finally:
            if sys_path_modified and project_str in sys.path:
                sys.path.remove(project_str)

    def _extract_imports(self, source_code: str) -> str:
        """Extract all import statements from a source string using AST."""
        imports = []
        try:
            tree = ast.parse(source_code)
            for node in ast.walk(tree):
                if isinstance(node, (ast.Import, ast.ImportFrom)):
                    imports.append(ast.unparse(node))
        except SyntaxError:
            pass  # Code fragment might not parse fully, ignore
        return "\n".join(imports)

    def _format_variable_state(self, variable_state: Dict[str, Any]) -> str:
        """Format a dictionary of variable states into a readable string."""
        lines = []
        for var, val in variable_state.items():
            if var == 'self':
                # Attempt to beautify 'self' object representation
                if hasattr(val, '__dict__'):
                     lines.append(f"self: {val} (attributes omitted for brevity)")
                else:
                     lines.append(f"self: {val}")
            else:
                lines.append(f"{var} = {val}")
        return "\n".join(lines)

    def run_test_case(self, test_code: str, project_dir: str, test_dir: str) -> Dict[str, Any]:
        """
        Execute the generated test case in a sandboxed temporary file.

        Args:
            test_code: The Python code of the test case.
            project_dir: The root directory of the project.
            test_dir: The directory to store temporary test files.

        Returns:
            Dictionary with keys: 'success', 'output', 'coverage', 'error'.
        """
        import unittest
        import io
        
        logger.info("-" * 40 + " Executing Test Case " + "-" * 40)
        
        original_cwd = os.getcwd()
        os.chdir(project_dir)

        stdout_buffer = io.StringIO()
        stderr_buffer = io.StringIO()
        
        result_data = {
            'test case': '',
            'success': False,
            'error': None,
            'output': '',
            'coverage': {}
        }
        
        temp_path = None
        
        try:
            # 1. Create Temporary Test File
            with tempfile.NamedTemporaryFile(suffix='.py', dir=test_dir, delete=False, mode='w', encoding='utf-8') as temp_file:
                temp_path = temp_file.name
                
                # Dynamic Import Generation
                try:
                    from ImportGenerator import ImportGenerator
                    import_gen = ImportGenerator(test_dir)
                    project_imports = import_gen.process_test_files()
                except ImportError:
                    logger.warning("ImportGenerator not found. Using minimal imports.")
                    project_imports = []

                # Assemble Full Code
                header_imports = [
                    f"import sys",
                    f"sys.path.insert(0, '{project_dir}')",
                    "import unittest",
                    "import timeout_decorator"
                ]
                
                full_source = "\n".join(header_imports + project_imports) + "\n\n" + test_code
                
                temp_file.write(full_source)
                result_data['test case'] = full_source

            # 2. Configure Coverage
            self.cov.erase()
            self.cov.start()
            
            # 3. Execute Test
            try:
                # Add temp dir to sys.path so we can import the temp module
                temp_dir = os.path.dirname(temp_path)
                if temp_dir not in sys.path:
                    sys.path.insert(0, temp_dir)

                with redirect_stdout(stdout_buffer), redirect_stderr(stderr_buffer):
                    module_name = os.path.splitext(os.path.basename(temp_path))[0]
                    
                    spec = importlib.util.spec_from_file_location(module_name, temp_path)
                    if spec and spec.loader:
                        test_module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(test_module)
                        
                        suite = unittest.TestLoader().loadTestsFromModule(test_module)
                        runner = unittest.TextTestRunner(stream=stdout_buffer, verbosity=2)
                        run_result = runner.run(suite)
                        
                        result_data['success'] = run_result.wasSuccessful()
            
            except Exception as e:
                result_data['error'] = str(e)
                logger.error(f"Runtime error during test execution: {e}")
                traceback.print_exc(file=stderr_buffer)
            finally:
                self.cov.stop()
                self.cov.save()
                
                if temp_dir in sys.path:
                    sys.path.remove(temp_dir)

            # 4. Process Coverage Data
            try:
                self.cov.json_report(outfile=os.devnull)  # Force data aggregation
                cov_data = self.cov.get_data()
                
                target_abspath = os.path.abspath(self.target_module_path)
                
                # Find matching file in coverage data
                for filename in cov_data.measured_files():
                    if os.path.abspath(filename) == target_abspath:
                        _, executable, missing, _ = self.cov.analysis(filename)
                        executed = list(set(executable) - set(missing))
                        
                        result_data['coverage'] = {
                            'covered_lines': executed,
                            'missing_lines': missing,
                            'total_lines': len(executable)
                        }
                        
                        pct = (len(executed) / len(executable) * 100) if executable else 0
                        logger.info(f"Test Coverage: {pct:.2f}% ({len(executed)}/{len(executable)})")
                        break
                        
            except Exception as e:
                logger.error(f"Failed to process coverage data: {e}")

        except Exception as e:
            result_data['error'] = str(e)
            logger.error(f"Critical error in run_test_case: {e}")
        
        finally:
            # 5. Cleanup
            os.chdir(original_cwd)
            result_data['output'] = stdout_buffer.getvalue() + stderr_buffer.getvalue()
            
            # Remove temp file
            if temp_path and os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                    # Try removing compiled bytecode
                    pyc = temp_path + 'c' # .pyc
                    if os.path.exists(pyc):
                        os.remove(pyc)
                except OSError as e:
                    logger.warning(f"Failed to clean up temp file {temp_path}: {e}")

        return result_data


def main():
    """Main entry point for command-line execution."""
    parser = argparse.ArgumentParser(description="LLM-based Test Case Generator")
    parser.add_argument("--api_key", required=True, help="OpenAI API Key")
    parser.add_argument("--module", required=True, help="Path to the target Python module")
    parser.add_argument("--project_dir", required=True, help="Path to the project root directory")
    parser.add_argument("--test_dir", required=True, help="Path to the directory containing existing tests")
    parser.add_argument("--output_dir", default="./generated_tests", help="Directory to save generated tests")
    parser.add_argument("--analysis_json", required=True, help="Path to 'similarity_analysis.json'")
    
    args = parser.parse_args()

    # Validate paths
    if not os.path.exists(args.module):
        logger.error(f"Target module not found: {args.module}")
        return

    generator = LLMTestGenerator(
        api_key=args.api_key,
        target_module_path=args.module
    )

    target_filename = os.path.basename(args.module)
    group_list = generator.parse_line_numbers_from_similarity_json(args.analysis_json, target_filename)

    if not group_list:
        logger.warning(f"No target line groups found for {target_filename} in {args.analysis_json}")
        return

    os.makedirs(args.output_dir, exist_ok=True)
    generator.coverage_trace_log_path = os.path.join(args.output_dir, "coverage_trace.jsonl")

    logger.info(f"Starting generation for {len(group_list)} groups...")

    for i, group in enumerate(group_list):
        logger.info(f"Processing Group {i + 1}/{len(group_list)}: Lines {group.get('line_numbers')}")
        
        record = generator.generate_tests(
            group=group,
            project_dir=args.project_dir,
            test_dir=args.test_dir,
            new_test_dir=args.output_dir,
            num_attempts=3
        )
        
        # Save generation record
        record_file = os.path.join(args.output_dir, "generation_records.jsonl")
        with open(record_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(record, ensure_ascii=False) + '\n')

    logger.info("Test generation completed.")


if __name__ == "__main__":
    main()