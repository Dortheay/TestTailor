from contextlib import nullcontext
import os
import json
from pickle import FALSE
from sqlite3 import complete_statement
from datetime import datetime
import traceback
import coverage
from coverage.misc import import_third_party
import openai
import ast
import re
import importlib
import tempfile
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Any
import inspect
import logging
from project_class_indexer import ProjectClassIndexer
import textwrap
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

class LLMTestGenerator:
    def __init__(
        self, 
        api_key: str,
        model_name: str = "gpt-4o-2024-11-20",
        target_module_path: str = None,
        max_retries: int = 2,
        temperature: float = 1,
        api_base: str = "https://api.openai.com/v1" 
    ):
        """
        初始化大模型测试用例生成器
        
        Args:
            api_key: API密钥
            model_name: 使用的模型名称
            target_module_path: 目标代码模块路径
            max_retries: 最大重试次数
            temperature: 生成多样性参数
            api_base: 自定义API基础URL（可选）
        """
        self.api_key = api_key
        self.model_name = model_name
        self.target_module_path = target_module_path
        self.max_retries = max_retries
        self.temperature = temperature
        self.api_base = api_base  
        
        
        with open(self.target_module_path, 'r', encoding='utf-8') as f:
            code = f.read()

        self.module_code = code

        # Get the module name and directory
        self.module_name = os.path.basename(target_module_path).replace('.py', '')
        self.module_dir = os.path.dirname(os.path.abspath(target_module_path))

        # Initialize the coverage measurement tool
        self.cov = coverage.Coverage(source=[target_module_path])
        
        # Store the successful test cases
        self.successful_tests = []
        
        # Load the target code
        self.target_code = self._load_target_code()
        
        # Initialize the message list, for maintaining the session history
        self.messages = []
        self.llm_total_call_count = 0  # 累计调用大模型次数
        self.coverage_trace_log_path = os.path.join(self.module_dir, "tiara_llm_call_vs_coverage.jsonl")  # 日志文件

        self.project_indexer = ProjectClassIndexer(self.module_dir)

    def _update_messages(self, prompt: str, role: str = "user", clear_history: bool = False):
        """
        Update the message history list
        
        Args:
            prompt: The prompt content to add
            role: The message role, can be "system", "user" or "assistant"
            clear_history: Whether to clear the history messages
        """
        if clear_history:
            self.messages = []
        
        # 如果是第一条消息且没有system消息，添加system消息
        if not self.messages or not any(msg["role"] == "system" for msg in self.messages):
            self.messages.append({
                "role": "system", 
                "content": "You are a professional Python test engineer, skilled in writing high-quality test cases."
            })
        
        # 添加新消息
        self.messages.append({
            "role": role,
            "content": prompt
        })    
   
    def _load_target_code(self) -> str:
        """Load the target code file content"""
        if not self.target_module_path or not os.path.exists(self.target_module_path):
            raise FileNotFoundError(f"The target code file does not exist: {self.target_module_path}")
        
        with open(self.target_module_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def _extract_functions_and_classes(self) -> Dict:
        """Extract the functions and classes from the target code"""
        try:
            tree = ast.parse(self.target_code)
            functions = []
            classes = []
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    functions.append({
                        'name': node.name,
                        'args': [arg.arg for arg in node.args.args],
                        'lineno': node.lineno,
                        'docstring': ast.get_docstring(node) or "No docstring"
                    })
                elif isinstance(node, ast.ClassDef):
                    methods = []
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef):
                            args = []
                            for arg in item.args.args:
                                if hasattr(arg, 'arg') and arg.arg != 'self':
                                    args.append(arg.arg)
                            methods.append({
                                'name': item.name,
                                'args': args,
                                'lineno': item.lineno,
                                'docstring': ast.get_docstring(item) or "No docstring"
                            })
                    
                    classes.append({
                        'name': node.name,
                        'methods': methods,
                        'lineno': node.lineno,
                        'docstring': ast.get_docstring(node) or "No docstring"
                    })
            
            return {
                'functions': functions,
                'classes': classes
            }
        except Exception as e:
            print(f"Error parsing the code: {str(e)}")
            return {'functions': [], 'classes': []}
    
    def _get_current_coverage(self, test_dir: str) -> Tuple[float, Dict]:
        """
        Execute the tests in test_dir and calculate the overall coverage of the current module
        """
        import unittest
        import io
        from contextlib import redirect_stdout
        import traceback

        print(f"Calculating the current coverage, test directory: {os.path.basename(test_dir)}")
        
        # 检查测试目录是否存在
        if not os.path.exists(test_dir):
            print(f"Error: The test directory does not exist: {test_dir}")
            return 0.0, {'error': 'The test directory does not exist'}
        
        # 检查测试目录中是否有测试文件
        test_files = [f for f in os.listdir(test_dir) if f.startswith('test_') and f.endswith('.py')]
        if not test_files:
            print(f"Warning: The test directory does not have any test files")
        else:
            print(f"Found {len(test_files)} test files")
        
        try:
            source_dir = os.path.dirname(os.path.abspath(self.target_module_path))
            data_file = os.path.join(self.module_dir, ".coverage")
            
            omit_patterns = [
                "*/tmp*.py",
                "*/__pycache__/*",
                "*/template*",
            ]
            
            self.cov = coverage.Coverage(
                source=[source_dir],
                data_file=data_file,
                omit=omit_patterns
            )
            
            self.cov.start()
            
            try:
                suite = unittest.defaultTestLoader.discover(test_dir)
                test_count = 0
                for test_suite in suite:
                    for test_case in test_suite:
                        test_count += test_case.countTestCases()
                print(f"Found {test_count} test cases")
                
                result_stream = io.StringIO()
                with redirect_stdout(result_stream):
                    result = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
                
                print(f"Test execution completed: runs={result.testsRun}, errors={len(result.errors)}, failures={len(result.failures)}")
                
                # 如果有错误或失败，打印简要信息
                if result.errors or result.failures:
                    print(f"Errors occurred during the test: {len(result.errors)} errors and {len(result.failures)} failures")
            
            except Exception as e:
                print(f"Error executing the test: {str(e)}")
            
            self.cov.stop()
            self.cov.save()
            
            data = self.cov.get_data()
            measured_files = list(data.measured_files())
            
            total_lines, covered_lines = 0, 0
            coverage_by_file = {}
            
            target_basename = os.path.basename(self.target_module_path)
            
            for file in measured_files:
                file_basename = os.path.basename(file)
                
                if file_basename == target_basename:
                    try:
                        analysis_result = self.cov.analysis(file)
                        _, executable, missing, excluded = analysis_result
                        
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
                        print(f"Error analyzing the file {file_basename}: {str(e)}")
            
            pct = covered_lines / total_lines * 100.0 if total_lines > 0 else 0.0
            print(f"Current coverage: {pct:.2f}% ({covered_lines}/{total_lines} lines)")
            
            result_dict = {
                'total_lines': total_lines,
                'covered_lines': covered_lines,
                'coverage_by_file': coverage_by_file
            }
            
            return pct, result_dict
        
        except Exception as e:
            print(f"Error calculating the coverage: {str(e)}")
            return 0.0, {'error': str(e)}

    def _build_initial_prompt(self, group: Dict, project_dir: str, test_dir: str) -> str:
        """
        Build the initial prompt (for attempt==1)
        """
        line_numbers = group.get('line_numbers', {})
        path_constraints = group.get("path_constraint", "")
        function_info = group.get('function_info', "")
        similarity_result = group.get('similarity_result', {})

        code_context = self.extract_context_by_line(line_numbers[0])

        prompt_sections = [
            self._build_function_under_test_section(code_context, line_numbers),
            self._build_path_constraint_section(path_constraints),
            self._build_similar_test_case_section(similarity_result, project_dir),
            self._build_task_instruction_section(function_info, test_dir)
        ]

        prompt = '\n'.join(filter(None, prompt_sections))
        print("In the initial stage, the prompt is \n" + prompt)
        return prompt

    def _build_function_under_test_section(self, code_context: dict, line_numbers: list) -> str:
        sections = []
        start_line, end_line = line_numbers[0], line_numbers[-1]

        if code_context['class_info'] and code_context['function_info']:
            sections.append("## Function under Test (with the class info)")
            sections.append("```python")
            sections.append(code_context['class_info']['complete_info'])
            sections.append(code_context['function_info']['code'])
            sections.append("```")
        elif code_context['function_info']:
            sections.append("## Function under Test")
            sections.append("```python")
            sections.append(code_context['function_info']['code'])
            sections.append("```")

        sections.append("## The Target code block you need to cover")
        sections.append("```python")
        sections.append(self._get_code_segment(start_line, end_line))
        sections.append("```")

        if code_context["related_project_classes"]:
            sections.append("## Related classes in the target function")
            for cls in code_context["related_project_classes"]:
                if cls.get("file"):
                    sections.append("The class is from file:" + cls["file"] + "\n")
                if cls.get("init_method"):  # 确保存在 init_method
                    sections.append("The definition of the class is as below: \n")
                    sections.append("```python")
                    sections.append(cls["init_method"])
                    sections.append("```")

        return '\n'.join(sections)

    def _build_path_constraint_section(self, path_constraints: str) -> str:
        if not path_constraints:
            return ""
        return f"""
To reach the target code, the test case needs to satisfy conditions along the path:
```python
{path_constraints}
```
"""

    def _build_similar_test_case_section(self, similarity_result: dict, project_dir: str) -> str:
        best_test_case = similarity_result.get('best_test_case')
        if not best_test_case:
            return ""

        test_case_code = self._get_test_case_code(best_test_case, project_dir)
        sections = [
            "## The most Path-Similar test case",
            "```python",
            test_case_code,
            "```"
        ]

        divergence = similarity_result.get('path_divergence', {})
        if divergence.get('has_divergence'):
            dp = divergence.get('divergence_point', {})
            div_line = dp.get('line', '')
            if div_line:
                divergence_code = self._get_code_segment(div_line, div_line)
                sections.append(f"""
## Path Divergence Analysis
The existing test case diverges from the target path at: {div_line}: {divergence_code}""")

            for kind in ['next_static', 'next_dynamic']:
                next_ = dp.get(kind, [None, None])
                if next_ and len(next_) >= 2:
                    line = next_[1]
                    try:
                        code = self._get_code_segment(line, line)
                    except Exception:
                        code = str(line)
                    label = "Target path continues to" if kind == 'next_static' else "Existing test path continues to"
                    sections.append(f"{label}: {line} : {code}")

            var_state = divergence.get('variable_state', {})
            if var_state and div_line:
                divergence_code = self._get_code_segment(div_line, div_line)
                important_vars = self._extract_code_variables(divergence_code, var_state)
                if important_vars:
                    sections.append("""
    At the Divergence Point, the similar test case has the following variable states:
    """ + self._format_variable_state(important_vars))

        return '\n'.join(sections)

    def _build_task_instruction_section(self, function_info: str, test_dir: str) -> str:
        from ImportGenerator import ImportGenerator
        import_gen = ImportGenerator(test_dir)
        imports = '\n'.join(import_gen.process_test_files())

        if "import unittest" not in imports:
            imports += "\nimport unittest"
        if "import timeout_decorator" not in imports:
            imports += "\nimport timeout_decorator"

        return f'''
## Your task
Create a test case that targets the branch containing our target code.
Use the reference test case as guidance and complete the function body only.
** Important: Only provide the completed test case starting from \"class Test\" line. Do not include import statements. **
```python
{imports}

class Test(unittest.TestCase):
    @timeout_decorator.timeout(1)
    def test_case_{function_info}(self):
        """complete the test case here"""
```
'''


    def _call_llm(self) -> str:
        """
        Call the LLM API (compatible with OpenAI 1.0.0+ version)
        
        Args:
            messages: The message list
            
        Returns:
            The response content of the LLM
        """
        try:
            if not self.messages:
                raise ValueError("Messages list is empty!")
            # 创建OpenAI客户端实例
            client = openai.OpenAI(
                api_key=self.api_key,
                base_url=getattr(self, 'api_base', None)  # 如果有自定义API基础URL，则使用它
            )
            
            # 调用API
            response = client.chat.completions.create(
                model=self.model_name,
                messages=self.messages,
                temperature=self.temperature,
                max_tokens=4000
            )
            self.llm_total_call_count += 1
            content = ""
            if hasattr(response, 'choices') and len(response.choices) > 0:
                content = response.choices[0].message.content
            # 新版API中，响应结构有所变化
            else:
                print("API response format exception, no choices field found")
                print(f"API response: {response}")
                return ""
            usage_info = {}
            if hasattr(response, 'usage') and response.usage:
                usage_info = {
                'prompt_tokens': response.usage.prompt_tokens,
                'completion_tokens': response.usage.completion_tokens,
                'total_tokens': response.usage.total_tokens
                }

            finish_reason = None
            if hasattr(response, 'choices') and len(response.choices) > 0:
                finish_reason = response.choices[0].finish_reason
            
            self._update_messages(content,"assistant",False)
            return {
                'content': content,
                'usage': usage_info,
                'finish_reason': finish_reason,
            }
        except Exception as e:
            print(f"Error calling the LLM API: {str(e)}")
            return ""

    def _extract_code_variables(self, code_line, variable_state):
        """
        Extract the variable names from the code line and get their values
        
        Args:
            code_line: The code line text
            variable_state: The dictionary containing the variable states
            
        Returns:
            The dictionary containing the variables and their values in the code line
        """
        if not code_line or not variable_state:
            return {}
        
        locals_vars = variable_state.get('locals', {})
        if not locals_vars:
            return {}
        
        # Use regular expression to extract possible variable names from the code
        import re
        # Match variable names but exclude keywords and content in strings/comments
        potential_vars = set(re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', code_line))
        
        # Exclude Python keywords and common built-in functions
        keywords = {
            'if', 'else', 'elif', 'for', 'while', 'try', 'except', 'with', 'return', 
            'and', 'or', 'not', 'in', 'is', 'True', 'False', 'None', 'class', 'def',
            'import', 'from', 'as', 'pass', 'break', 'continue', 'print', 'len',
            'str', 'int', 'float', 'list', 'dict', 'set', 'tuple'
        }
        
        # Filter out variables that exist in locals_vars
        relevant_vars = {}
        for var_name in potential_vars:
            if var_name in locals_vars and var_name not in keywords:
                var_value = locals_vars[var_name]
                
                # Simplify the representation of the value
                if var_name in ['node', 'body'] and isinstance(var_value, dict) and 'class' in var_value:
                    # For AST nodes, only extract type information
                    node_class = var_value.get('class')
                    if node_class == 'If':
                        # For If nodes, extract the condition value
                        try:
                            test_node = var_value.get('attributes', {}).get('test', {})
                            if test_node.get('class') == 'Constant':
                                test_value = test_node.get('attributes', {}).get('value')
                                relevant_vars[var_name] = f"If node with condition: {test_value}"
                            else:
                                relevant_vars[var_name] = f"If node"
                        except:
                            relevant_vars[var_name] = f"{node_class} node"
                    else:
                        relevant_vars[var_name] = f"{node_class} node"
                elif isinstance(var_value, dict) and len(var_value) > 3:
                    # For large dictionaries, only show the number of keys and some keys
                    keys = list(var_value.keys())[:3]
                    relevant_vars[var_name] = f"dict with {len(var_value)} keys: {keys}..."
                elif isinstance(var_value, (list, tuple)) and len(var_value) > 3:
                    # For large lists/tuples, only show the length and some elements
                    relevant_vars[var_name] = f"{type(var_value).__name__} with {len(var_value)} items"
                elif isinstance(var_value, str) and len(var_value) > 100:
                    # For long strings, only show some content
                    relevant_vars[var_name] = f"{var_value[:50]}... (length: {len(var_value)})"
                else:
                    # For simple values, display them directly
                    relevant_vars[var_name] = var_value
        
        # Handle self references
        self_attrs = re.findall(r'self\.([a-zA-Z_][a-zA-Z0-9_]*)', code_line)
        if self_attrs and 'self' in locals_vars:
            self_obj = locals_vars['self']
            if hasattr(self_obj, '__dict__'):
                self_dict = getattr(self_obj, '__dict__', {})
                for attr in self_attrs:
                    if attr in self_dict:
                        relevant_vars[f"self.{attr}"] = self_dict[attr]
        
        return relevant_vars


    def _extract_test_code(self, llm_response: str) -> str:
        """
        Use a greedy regular expression to achieve the same functionality.
        """
        if not llm_response or not isinstance(llm_response, str):
            return ""

        # (.*) 在 re.DOTALL 模式下会尽可能多地匹配字符（贪婪）
        # 它会从第一个 '```python' 一直匹配到最后一个 '```'
        match = re.search(r'```python(.*)```', llm_response, re.DOTALL)
        
        if match:
            # group(1) 获取第一个捕获组的内容，并去除首尾空格
            return match.group(1).strip()
        
        return ""


    def _generate_error_fix_prompt(self, test_code: str, error_message: str, test_dir:str) -> str:
        """Generate the error fix prompt"""

        # from ImportGenerator import ImportGenerator
        # importGenerator = ImportGenerator(test_dir)
        # unique_imports = importGenerator.process_test_files()
        # imports = ""
        # for import_s in unique_imports:
        #         imports += import_s
        #         imports += '\n'
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
        self._update_messages(prompt, "user", False)
        return prompt

    ## Initial version 只有完全覆盖了目标代码块的，才算成功覆盖
    def generate_tests_strict(self, group: Dict, project_dir: str, test_dir: str, new_test_dir: str, num_attempts: int = 3) -> Dict:
        """
        Generate and verify the main flow of test cases
        
        Args:
            num_attempts: The number of attempts to generate test cases
            new_test_dir: The location where the new test cases are generated
        Returns:
            The dictionary containing the test generation details
        """
        generation_record = {
            "timestamp": datetime.now().isoformat(),
            "target_module": self.target_module_path,
            "target_lines": group['line_numbers'],
            "project_dir": str(project_dir),
            "test_dir": str(test_dir),
            "new_test_dir": str(new_test_dir),
            "attempts": [],
            "total_usage": {
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0
            },
            "final_result": {
                "success": False,
                "test_file_path": None,
                "test_code": None,
                "coverage_info": None
            }
        }
        
        initial_prompt = self._build_initial_prompt(group, project_dir, test_dir)
        self._update_messages(initial_prompt, "user", clear_history=True)
        response = llmgenerator._call_llm()
        
        # Record the first attempt
        attempt_record = {
            "attempt_number": 1,
            "prompt_type": "initial",
            "llm_usage": response['usage'],
            "finish_reason": response['finish_reason']
        }
        
        # Accumulate the usage
        if response.get('usage'):
            for key in generation_record["total_usage"]:
                generation_record["total_usage"][key] += response['usage'].get(key, 0)
        
        test_code = llmgenerator._extract_test_code(response['content'])
        test_result = llmgenerator.run_test_case(test_code, project_dir, test_dir)    

        attempt_record.update({
            "test_code": test_code,
            "test_execution_success": test_result['success'],
            "test_output": test_result.get('output', ''),
            "coverage_info": test_result.get('coverage', {}),
            "covered_lines": test_result['coverage'].get('covered_lines', []) if test_result.get('coverage') else []
        })

        group_lines = set(group['line_numbers'])
        # Safely get the covered lines
        result_lines = set(test_result['coverage']['covered_lines']) if test_result.get('coverage') and test_result['coverage'].get('covered_lines') else set()

        if test_result['success'] and group_lines.issubset(result_lines):
            print(f"Successfully covered {group['line_numbers']}")  # 修复：使用 f-string
            
            os.makedirs(new_test_dir, exist_ok=True)
            module_name = os.path.basename(self.target_module_path)
            if module_name.endswith('.py'):
                module_name = module_name[:-3]
            first_line = group["line_numbers"][0] if group["line_numbers"] else 0
            test_file_name = f"test_{module_name}_line{first_line}.py"
            test_file_path = os.path.join(new_test_dir, test_file_name)
            
            with open(test_file_path, 'w', encoding='utf-8') as f:
                f.write(test_result['test case'])
            
            # Update the final result
            generation_record["final_result"] = {
                "success": True,
                "test_file_path": str(test_file_path),
                "test_file_name": test_file_name,
                "test_code": test_result['test case'],
                "coverage_info": test_result.get('coverage', {}),
                "covered_lines": list(result_lines),
                "target_lines_covered": list(group_lines),
                "lines_not_covered": []
            }
            
            attempt_record["result"] = "success"
            self.successful_tests.append(test_result['test case'])  # Only add once
            
        else:
            attempt_record["result"] = "failed"
            attempt_record["failure_reason"] = "execution_failed" if not test_result['success'] else "insufficient_coverage"
            attempt_record["lines_not_covered"] = list(group_lines - result_lines)
            
            for attempt in range(num_attempts - 1):
                print(f"\n尝试 {attempt + 1}/{num_attempts - 1} 修复测试用例...")
                retry_record = {
                    "attempt_number": attempt + 2,
                    "prompt_type": None,
                    "previous_failure": attempt_record["failure_reason"] if attempt == 0 else generation_record["attempts"][-1]["failure_reason"]
                }
                
                if test_result['success']:
                    print(f"测试运行成功，但未覆盖所需行: {group_lines - result_lines}")
                    self._update_messages(initial_prompt, "user", True)
                    retry_record["prompt_type"] = "coverage_fix"
                else:
                    print(f"测试运行失败: {test_result.get('output', '未知错误')}")
                    self._generate_error_fix_prompt(test_result['test case'], test_result['output'], test_dir)
                    retry_record["prompt_type"] = "error_fix"
                
                response = llmgenerator._call_llm()
                
                # Accumulate the usage of the retries
                retry_record.update({
                    "llm_usage": response.get('usage', {}),
                    "finish_reason": response.get('finish_reason', None)
                })
                
                if response.get('usage'):
                    for key in generation_record["total_usage"]:
                        generation_record["total_usage"][key] += response['usage'].get(key, 0)
                
                test_code = llmgenerator._extract_test_code(response['content'])
                test_result = llmgenerator.run_test_case(test_code, project_dir, test_dir)
                result_lines = set(test_result['coverage']['covered_lines']) if test_result.get('coverage') and test_result['coverage'].get('covered_lines') else set()

                # Record the result of the retries
                retry_record.update({
                    "test_code": test_code,
                    "test_execution_success": test_result['success'],
                    "test_output": test_result.get('output', ''),
                    "coverage_info": test_result.get('coverage', {}),
                    "covered_lines": list(result_lines)
                })

                if test_result['success'] and group_lines.issubset(result_lines):
                    print(f"After fixing, successfully covered {group['line_numbers']}")
                    os.makedirs(new_test_dir, exist_ok=True)
                    module_name = os.path.basename(self.target_module_path)
                    if module_name.endswith('.py'):
                        module_name = module_name[:-3]
                    first_line = group["line_numbers"][0] if group["line_numbers"] else 0
                    test_file_name = f"test_{module_name}_line{first_line}.py"
                    test_file_path = os.path.join(new_test_dir, test_file_name)
                    
                    with open(test_file_path, 'w', encoding='utf-8') as f:
                        f.write(test_result['test case'])
                    
                    generation_record["final_result"] = {
                        "success": True,
                        "test_file_path": str(test_file_path),
                        "test_file_name": test_file_name,
                        "test_code": test_result['test case'],
                        "coverage_info": test_result.get('coverage', {}),
                        "covered_lines": list(result_lines),
                        "target_lines_covered": list(group_lines),
                        "lines_not_covered": []
                    }
                    
                    retry_record["result"] = "success"
                    self.successful_tests.append(test_result['test case'])
                    generation_record["attempts"].append(retry_record)
                    break  
                else:
                    retry_record["result"] = "failed"
                    retry_record["failure_reason"] = "execution_failed" if not test_result['success'] else "insufficient_coverage"
                    retry_record["lines_not_covered"] = list(group_lines - result_lines)                  
                
                generation_record["attempts"].append(retry_record)
        
        # Add the first attempt to the record
        generation_record["attempts"].insert(0, attempt_record)

        # If the final result is not successful, record the failure information
        if not generation_record["final_result"]["success"]:
            generation_record["final_result"]["lines_not_covered"] = list(group_lines - result_lines)


        print(f"总Token使用量: {generation_record['total_usage']}")

        return generation_record

    def generate_tests(self, group: Dict, project_dir: str, test_dir: str, new_test_dir: str, num_attempts: int = 3) -> Dict:
        generation_record = {
            "timestamp": datetime.now().isoformat(),
            "target_module": self.target_module_path,
            "target_lines": group['line_numbers'],
            "project_dir": str(project_dir),
            "test_dir": str(test_dir),
            "new_test_dir": str(new_test_dir),
            "attempts": [],
            "total_usage": {
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0
            },
            "final_result": {
                "success": False,
                "test_file_path": None,
                "test_code": None,
                "coverage_info": None
            }
        }

        # Get the current coverage baseline
        print(f"Getting the current coverage baseline...")
        _, cov_detail = self._get_current_coverage(str(new_test_dir))
        previously_covered = set()
        for f in cov_detail.get("coverage_by_file", {}).values():
            previously_covered.update(f.get("executed_lines", []))

        # Build the initial prompt and call the LLM
        print(f"Building the initial prompt and calling the LLM...")
        initial_prompt = self._build_initial_prompt(group, project_dir, test_dir)
        self._update_messages(initial_prompt, "user", clear_history=True)
        response = self._call_llm()

        attempt_record = {
            "attempt_number": 1,
            "prompt_type": "initial",
            "llm_usage": response['usage'],
            "finish_reason": response['finish_reason']
        }

        # Accumulate the token usage
        if response.get('usage'):
            for key in generation_record["total_usage"]:
                generation_record["total_usage"][key] += response['usage'].get(key, 0)

        # Extract the test code and execute it
        print(f"Extracting the test code and executing it...")
        test_code = self._extract_test_code(response['content'])
        test_result = self.run_test_case(test_code, project_dir, test_dir)
        result_lines = set(test_result['coverage'].get('covered_lines', [])) if test_result.get('coverage') else set()
        newly_covered = result_lines - previously_covered

        attempt_record.update({
            "test_code": test_code,
            "test_execution_success": test_result['success'],
            "test_output": test_result.get('output', ''),
            "coverage_info": test_result.get('coverage', {}),
            "covered_lines": list(result_lines),
            "newly_covered_lines": list(newly_covered)
        })

        # Check if the test is successful and has increased coverage
        if test_result['success'] and newly_covered:
            print(f"✅ Successfully covered the target lines: {group['line_numbers']}")
            
            # Save the test file
            os.makedirs(new_test_dir, exist_ok=True)
            module_name = os.path.basename(self.target_module_path)
            if module_name.endswith('.py'):
                module_name = module_name[:-3]
            first_line = group["line_numbers"][0] if group["line_numbers"] else 0
            test_file_name = f"test_{module_name}_line{first_line}.py"
            test_file_path = os.path.join(new_test_dir, test_file_name)
            
            with open(test_file_path, 'w', encoding='utf-8') as f:
                f.write(test_result['test case'])

            # Update the result record
            generation_record["final_result"] = {
                "success": True,
                "test_file_path": str(test_file_path),
                "test_file_name": os.path.basename(test_file_path),
                "test_code": test_result['test case'],
                "coverage_info": test_result.get('coverage', {}),
                "covered_lines": list(result_lines),
                "target_lines_covered": list(group['line_numbers']),
                "lines_not_covered": list(set(group['line_numbers']) - result_lines)
            }
            attempt_record["result"] = "success"
            self.successful_tests.append(test_result['test case'])

            # Record the coverage log
            overall_pct, _ = self._get_current_coverage(str(new_test_dir))
            with open(self.coverage_trace_log_path, 'a', encoding='utf-8') as f:
                f.write(json.dumps({
                    "timestamp": datetime.now().isoformat(),
                    "module": self.target_module_path,
                    "total_llm_calls": self.llm_total_call_count,
                    "current_coverage_pct": round(overall_pct, 2),
                    "test_dir": str(test_dir)
                }, ensure_ascii=False) + '\n')
        else:
            # The test failed or did not increase coverage
            if not test_result['success']:
                print(f"❌ The test execution failed")
                print(f"Error information: {test_result.get('output', '')[:]}")
            else:
                print(f"❌ The test execution succeeded but did not increase coverage")
                print(f"Target lines: {group['line_numbers']}")
                print(f"Covered lines: {list(result_lines)[:]}")
                
            attempt_record["result"] = "failed"
            attempt_record["failure_reason"] = "execution_failed" if not test_result['success'] else "no_new_coverage"
            attempt_record["lines_not_covered"] = list(set(group['line_numbers']) - result_lines)

            # Retry logic
            for attempt in range(1, num_attempts):
                print(f"\n尝试 {attempt+1}/{num_attempts}: {'修复执行错误' if not test_result['success'] else '提高覆盖率'}...")
                retry_record = {
                    "attempt_number": attempt + 1,
                    "prompt_type": None,
                    "previous_failure": attempt_record["failure_reason"]
                }

                # Build different prompts based on the failure type
                if test_result['success']:
                    self._update_messages(initial_prompt, "user", True)
                    retry_record["prompt_type"] = "coverage_fix"
                else:
                    self._generate_error_fix_prompt(test_result['test case'], test_result['output'], test_dir)
                    retry_record["prompt_type"] = "error_fix"

                # Call the LLM to get the repaired test
                response = self._call_llm()
                retry_record.update({
                    "llm_usage": response.get('usage', {}),
                    "finish_reason": response.get('finish_reason', None)
                })

                # Accumulate the token usage
                if response.get('usage'):
                    for key in generation_record["total_usage"]:
                        generation_record["total_usage"][key] += response['usage'].get(key, 0)

                # Extract and execute the repaired test code
                test_code = self._extract_test_code(response['content'])
                test_result = self.run_test_case(test_code, project_dir, test_dir)
                result_lines = set(test_result['coverage'].get('covered_lines', [])) if test_result.get('coverage') else set()
                newly_covered = result_lines - previously_covered

                retry_record.update({
                    "test_code": test_code,
                    "test_execution_success": test_result['success'],
                    "test_output": test_result.get('output', ''),
                    "coverage_info": test_result.get('coverage', {}),
                    "covered_lines": list(result_lines),
                    "newly_covered_lines": list(newly_covered)
                })

                # Check if the retry is successful
                if test_result['success'] and newly_covered:
                    print(f"✅ The retry is successful! Covered the target lines: {group['line_numbers']}")
                    
                    # Save the successful test
                    os.makedirs(new_test_dir, exist_ok=True)
                    module_name = os.path.basename(self.target_module_path)
                    if module_name.endswith('.py'):
                        module_name = module_name[:-3]
                    first_line = group["line_numbers"][0] if group["line_numbers"] else 0
                    test_file_name = f"test_{module_name}_line{first_line}.py"
                    test_file_path = os.path.join(new_test_dir, test_file_name)
                    
                    with open(test_file_path, 'w', encoding='utf-8') as f:
                        f.write(test_result['test case'])

                    # Update the result record
                    generation_record["final_result"] = {
                        "success": True,
                        "test_file_path": str(test_file_path),
                        "test_file_name": os.path.basename(test_file_path),
                        "test_code": test_result['test case'],
                        "coverage_info": test_result.get('coverage', {}),
                        "covered_lines": list(result_lines),
                        "target_lines_covered": list(group['line_numbers']),
                        "lines_not_covered": list(set(group['line_numbers']) - result_lines)
                    }
                    retry_record["result"] = "success"
                    self.successful_tests.append(test_result['test case'])

                    # Record the coverage log
                    overall_pct, _ = self._get_current_coverage(str(new_test_dir))
                    with open(self.coverage_trace_log_path, 'a', encoding='utf-8') as f:
                        f.write(json.dumps({
                            "timestamp": datetime.now().isoformat(),
                            "module": self.target_module_path,
                            "total_llm_calls": self.llm_total_call_count,
                            "current_coverage_pct": round(overall_pct, 2),
                            "test_dir": str(test_dir)
                        }, ensure_ascii=False) + '\n')
                    generation_record["attempts"].append(retry_record)
                    break
                else:
                    # The retry failed
                    if not test_result['success']:
                        print(f"❌ The retry {attempt+1} execution failed")
                        print(f"Error information: {test_result.get('output', '')[:]}...")
                    else:
                        print(f"❌ The retry {attempt+1} execution succeeded but did not increase coverage")
                    
                    retry_record["result"] = "failed"
                    retry_record["failure_reason"] = "execution_failed" if not test_result['success'] else "no_new_coverage"
                    retry_record["lines_not_covered"] = list(set(group['line_numbers']) - result_lines)
                    generation_record["attempts"].append(retry_record)

        # Add the first attempt record
        generation_record["attempts"].insert(0, attempt_record)

        # If all attempts failed, record the final result
        if not generation_record["final_result"]["success"]:
            generation_record["final_result"]["lines_not_covered"] = list(set(group['line_numbers']) - result_lines)

        # Save the complete prompt message history
        import copy
        generation_record["final_prompt_messages"] = copy.deepcopy(self.messages)
        print(f"Total token usage: {generation_record['total_usage']}")
        return generation_record


    def save_successful_tests(self, output_path: str = None):
        """Save all successful test cases to a file"""
        if not self.successful_tests:
            print("No successful test cases to save")
            return
        
        if output_path is None:
            output_path = f"generated_tests_{self.module_name}.py"
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# Automatically generated test cases\n")
            f.write(f"import pytest\nfrom {self.module_name} import *\n\n")
            
            for i, test in enumerate(self.successful_tests):
                f.write(f"# Test case {i+1}\n")
                # Remove possible duplicate import statements in the test code
                cleaned_test = re.sub(r'import pytest.*?\n', '', test)
                cleaned_test = re.sub(r'from.*?import.*?\n', '', cleaned_test)
                f.write(cleaned_test)
                f.write("\n\n")
        
        print(f"Successfully saved {len(self.successful_tests)} test cases to {output_path}")

    # Record each line_numbers for subsequent prompt construction
    @staticmethod
    def parse_line_numbers_from_similarity_json(json_path: str, target_filename: str) -> List[List[int]]:
        """
        Parse the similarity_analysis.json file, extract the line_numbers list for all groups in the target file
        Args:
            json_path: json file path
            target_filename: target file name (e.g. 'loader.py')
        Returns:
            line_numbers_list: the line_numbers list for all groups in the target file (each group is a list)
        """
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"JSON file not found: {json_path}")
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        suggestions = data.get('suggestions_analysis', {})
        if target_filename not in suggestions:
            return []
        line_numbers_list = []
        # print(type(suggestions[target_filename]))
        return suggestions[target_filename]
        # for group in suggestions[target_filename]:
        #     # TODO: Pass it on
        #     print(f"Group type: {type(group)}")
        #     self._build_prompt(1,group)
        #     print("Here call the build prompt function to construct")
        # return line_numbers_list

    ## Below is the function and class information of the line_number that must be found
    def build_code_structure(self) -> Dict[str, Any]:
        """
        Parse the entire file, build the code structure mapping, including the relationship between functions and classes
        
        Returns:
            The dictionary containing the code structure, including:
            - classes: class information list, each class contains the name, line number range, and methods
            - functions: function information list, each function contains the name, line number range, and所属类等
            - line_to_context: line number to context mapping
        """
        # Use AST to parse the entire code
        try:
            tree = ast.parse(self.module_code)
        except SyntaxError:
            # If the code has a syntax error, return an empty structure
            return {
                "classes": [],
                "functions": [],
                "line_to_context": {}
            }
        
        # Initialize the structure
        structure = {
            "classes": [],
            "functions": [],
            "line_to_context": {}  # line number -> {function, class}
        }
        
        # Find all class and function definitions
        for node in ast.walk(tree):
            # Process class definitions
            if isinstance(node, ast.ClassDef):
                # Find the end line of the class
                end_line = 0
                for child in node.body:
                    if hasattr(child, 'lineno'):
                        end_line = max(end_line, getattr(child, 'end_lineno', child.lineno))
                
                # If the end line is not found, use the line number of the next sibling node minus 1 or the end of the file
                if end_line == 0:
                    # Find the next sibling node
                    next_sibling_line = float('inf')
                    for sibling in ast.iter_child_nodes(tree):
                        if (isinstance(sibling, (ast.ClassDef, ast.FunctionDef)) and 
                            sibling.lineno > node.lineno):
                            next_sibling_line = min(next_sibling_line, sibling.lineno)
                    
                    end_line = next_sibling_line - 1 if next_sibling_line < float('inf') else len(self.module_code.split('\n'))
                
                # Collect the class decorators
                class_decorators = []
                for decorator in node.decorator_list:
                    if isinstance(decorator, ast.Name):
                        class_decorators.append(decorator.id)
                    elif isinstance(decorator, ast.Call) and isinstance(decorator.func, ast.Name):
                        class_decorators.append(f"{decorator.func.id}(...)")
                    elif isinstance(decorator, ast.Attribute):
                        class_decorators.append(self._get_attribute_name(decorator))
                
                # Extract the class docstring
                class_docstring = ast.get_docstring(node)
                
                # Collect the class methods
                methods = []
                init_method = None
                
                for child in node.body:
                    if isinstance(child, ast.FunctionDef):
                        # Collect the method decorators
                        method_decorators = []
                        for decorator in child.decorator_list:
                            if isinstance(decorator, ast.Name):
                                method_decorators.append(decorator.id)
                            elif isinstance(decorator, ast.Call) and isinstance(decorator.func, ast.Name):
                                method_decorators.append(f"{decorator.func.id}(...)")
                            elif isinstance(decorator, ast.Attribute):
                                method_decorators.append(self._get_attribute_name(decorator))
                        
                        # Find the actual start line of the method (including decorators)
                        actual_start_line = child.lineno
                        if child.decorator_list and hasattr(child.decorator_list[0], 'lineno'):
                            actual_start_line = child.decorator_list[0].lineno
                        
                        method_end_line = getattr(child, 'end_lineno', child.lineno)
                        for stmt in child.body:
                            if hasattr(stmt, 'lineno'):
                                method_end_line = max(method_end_line, getattr(stmt, 'end_lineno', stmt.lineno))
                        
                        # Extract the method docstring
                        method_docstring = ast.get_docstring(child)
                        
                        method_info = {
                            "name": child.name,
                            "start_line": child.lineno,  # function definition line
                            "actual_start_line": actual_start_line,  # actual start line including decorators
                            "end_line": method_end_line,
                            "params": [arg.arg for arg in child.args.args],
                            "decorators": method_decorators,
                            "docstring": method_docstring
                        }
                        
                        methods.append(method_info)
                        
                        # Record the init method
                        if child.name == "__init__":
                            init_method = method_info
                
                # Create class information
                class_info = {
                    "name": node.name,
                    "start_line": node.lineno,
                    "end_line": end_line,
                    "methods": methods,
                    "init_method": init_method,
                    "decorators": class_decorators,
                    "docstring": class_docstring
                }
                
                structure["classes"].append(class_info)
                
                # Create a mapping for each line of the class
                for line in range(node.lineno, end_line + 1):
                    structure["line_to_context"][line] = {
                        "class": class_info,
                        "function": None
                    }
                
                # Create a mapping for each method in the class
                for method in methods:
                    for line in range(method["actual_start_line"], method["end_line"] + 1):
                        structure["line_to_context"][line] = {
                            "class": class_info,
                            "function": method
                        }
            
            # Process independent function definitions
            elif isinstance(node, ast.FunctionDef) and not any(
                node.lineno >= class_info["start_line"] and node.lineno <= class_info["end_line"]
                for class_info in structure["classes"]
            ):
                # Collect the function decorators
                func_decorators = []
                for decorator in node.decorator_list:
                    if isinstance(decorator, ast.Name):
                        func_decorators.append(decorator.id)
                    elif isinstance(decorator, ast.Call) and isinstance(decorator.func, ast.Name):
                        func_decorators.append(f"{decorator.func.id}(...)")
                    elif isinstance(decorator, ast.Attribute):
                        func_decorators.append(self._get_attribute_name(decorator))
                
                # Find the actual start line of the function (including decorators)
                actual_start_line = node.lineno
                if node.decorator_list and hasattr(node.decorator_list[0], 'lineno'):
                    actual_start_line = node.decorator_list[0].lineno
                
                # Find the end line of the function
                end_line = getattr(node, 'end_lineno', node.lineno)
                for stmt in node.body:
                    if hasattr(stmt, 'lineno'):
                        end_line = max(end_line, getattr(stmt, 'end_lineno', stmt.lineno))
                
                # Extract the function docstring
                func_docstring = ast.get_docstring(node)
                
                # Create function information
                function_info = {
                    "name": node.name,
                    "start_line": node.lineno,  # function definition line
                    "actual_start_line": actual_start_line,  # actual start line including decorators
                    "end_line": end_line,
                    "params": [arg.arg for arg in node.args.args],
                    "decorators": func_decorators,
                    "docstring": func_docstring,
                    "class": None  # independent function does not belong to any class
                }
                
                structure["functions"].append(function_info)
                
                # Create a mapping for each line of the function
                for line in range(actual_start_line, end_line + 1):
                    structure["line_to_context"][line] = {
                        "class": None,
                        "function": function_info
                    }
        
        # Extract the comments of the class and function (not docstrings)
        self._extract_comments(structure)
        
        return structure
    
    def _get_attribute_name(self, node):
        """Recursively get the attribute name, e.g. module.submodule.function"""
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            return f"{self._get_attribute_name(node.value)}.{node.attr}"
        return "unknown"

    def _extract_comments(self, structure):
        """Extract the comments of the class and function definition (not docstrings)"""
        lines = self.module_code.split('\n')
        
        # Process the comments of the class
        for class_info in structure["classes"]:
            class_line = class_info["start_line"]
            
            # Check the comments after the class definition
            class_header_comments = []
            current_line = class_line
            
            # If the class has a docstring, skip the docstring line
            if class_info["docstring"]:
                # Simple estimate the number of lines in the docstring (this is an approximation)
                docstring_lines = class_info["docstring"].count('\n') + 3  # add quotes and possible empty lines
                current_line += docstring_lines
            else:
                # No docstring, check the next line
                current_line += 1
            
            # Collect the comments after the class definition
            while current_line < len(lines) and current_line < class_info["end_line"]:
                line = lines[current_line - 1].strip()
                # If it is an empty line or already reached the first method, stop collecting
                if not line or (line and not line.startswith('#')):
                    if any(method["start_line"] == current_line for method in class_info["methods"]):
                        break
                    if not line:  # empty line continue
                        current_line += 1
                        continue
                    break
                
                # Collect the comments lines
                class_header_comments.append(line)
                current_line += 1
            
            class_info["header_comments"] = class_header_comments
        
        # Process the comments of the function
        for function_info in structure["functions"]:
            function_line = function_info["start_line"]
            
            # Check the comments after the function definition
            function_header_comments = []
            current_line = function_line
            
            # If the function has a docstring, skip the docstring line
            if function_info["docstring"]:
                # Simple estimate the number of lines in the docstring
                docstring_lines = function_info["docstring"].count('\n') + 3
                current_line += docstring_lines
            else:
                # No docstring, check the next line
                current_line += 1
            
            # Collect the comments after the function definition
            while current_line < len(lines) and current_line < function_info["end_line"]:
                line = lines[current_line - 1].strip()
                # If it is an empty line or already reached the function body, stop collecting
                if not line or (line and not line.startswith('#')):
                    break
                
                # Collect the comments lines
                function_header_comments.append(line)
                current_line += 1
            
            function_info["header_comments"] = function_header_comments
        
        # Similarly process the methods in the class
        for class_info in structure["classes"]:
            for method_info in class_info["methods"]:
                method_line = method_info["start_line"]
                
                # Check the comments after the method definition
                method_header_comments = []
                current_line = method_line
                
                        # If the method has a docstring, skip the docstring line
                if method_info["docstring"]:
                    # Simple estimate the number of lines in the docstring
                    docstring_lines = method_info["docstring"].count('\n') + 3
                    current_line += docstring_lines
                else:
                    # No docstring, check the next line
                    current_line += 1
                
                # Collect the comments after the method definition
                while current_line < len(lines) and current_line < method_info["end_line"]:
                    line = lines[current_line - 1].strip()
                    # If it is an empty line or already reached the method body, stop collecting
                    if not line or (line and not line.startswith('#')):
                        break
                    
                    # Collect the comments lines
                    method_header_comments.append(line)
                    current_line += 1
                
                method_info["header_comments"] = method_header_comments

    def _extract_used_classes(self, function_code: str) -> set:
        """Extract the class names used in the function source code"""
        used_classes = set()
        try:
            dedented_code = textwrap.dedent(function_code)   # Remove the indentation
            tree = ast.parse(dedented_code)
            for node in ast.walk(tree):
                # 1. Class instantiation
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                    used_classes.add(node.func.id)
                # 2. Type annotations
                elif isinstance(node, ast.Name):
                    used_classes.add(node.id)
                # 3. Class inheritance
                elif isinstance(node, ast.ClassDef):
                    for base in node.bases:
                        if isinstance(base, ast.Name):
                            used_classes.add(base.id)
                # 4. Static method call Foo.bar()
                elif isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
                    used_classes.add(node.value.id)
        except Exception as e:
            print(f"[WARN] AST parsing failed: {e}")
        return used_classes

    def extract_context_by_line(self, line_number: int) -> Dict[str, Any]:
        """
        Extract the code context information by line number, return the structured class and function information
        
        Args:
            line_number: code line number
        
        Returns:
            A dictionary containing the context information, including:
            - function_info: function information (if the line is in the function)
            - class_info: class information (if the line is in the class), including the complete class definition and init method
        """
        # print("line number is " + str(line_number))
        # If the code structure has not been built, build it first
        if not hasattr(self, '_code_structure'):
            self._code_structure = self.build_code_structure()
        
        # Get the context corresponding to the line number
        context = self._code_structure["line_to_context"].get(line_number, {"class": None, "function": None})
        
        result = {
            "function_info": None,
            "class_info": None
        }
        
        # Extract the function information
        if context["function"]:
            function = context["function"]
            # Get the complete function code (including decorators)
            full_function_code = self._get_code_segment(function["actual_start_line"], function["end_line"])
            
            # Add line numbers to the function code
            function_lines = full_function_code.split('\n')
            numbered_function_code = '\n'.join(f"{function['actual_start_line'] + i}: {line}" 
                                            for i, line in enumerate(function_lines))
            
            result["function_info"] = {
                "name": function["name"],
                "params": ", ".join(function["params"]),
                "line_number": function["start_line"],
                "actual_start_line": function["actual_start_line"],
                "end_line": function["end_line"],
                "decorators": function.get("decorators", []),
                "docstring": function.get("docstring"),
                "header_comments": function.get("header_comments", []),
                "numbered_code": numbered_function_code,
                "code": full_function_code
            }
        
        result["related_project_classes"] = []

        if result["function_info"]:
            used_classes = self._extract_used_classes(result["function_info"]["code"])
            for cls_name in used_classes:
                cls_info = self.project_indexer.get_class_info(cls_name)
                if cls_info:
                    result["related_project_classes"].append(cls_info)

        # Extract the class information
        if context["class"]:
            class_info = context["class"]
            
            # Build the complete class definition information (including decorators, class name, docstring)
            class_definition_lines = []
            
            # 1. Add decorators
            decorators = class_info.get("decorators", [])
            for decorator in decorators:
                class_definition_lines.append(f"{decorator}")
            
            # 2. Add class definition line
            class_definition_lines.append(f"class {class_info['name']}:")
            
            # 3. Add docstring
            if class_info.get("docstring"):
                docstring = class_info["docstring"]
                if '\n' in docstring:
                    class_definition_lines.append('    """')
                    for line in docstring.split('\n'):
                        class_definition_lines.append(f"    {line}")
                    class_definition_lines.append('    """')
                else:
                    class_definition_lines.append(f'    """{docstring}"""')
            
            # 4. Add header comments
            for comment in class_info.get("header_comments", []):
                class_definition_lines.append(f"    {comment}")
            
            # Add line numbers to the class definition
            class_definition = '\n'.join(class_definition_lines)
            numbered_class_definition = '\n'.join(
                f"{class_info['start_line'] - len(decorators) + i}: {line}" 
                for i, line in enumerate(class_definition_lines)
            )
            
            # Process the init method
            init_info = None
            init_code = ""
            if class_info["init_method"]:
                init = class_info["init_method"]
                # Get the complete init method code (including decorators)
                init_code = self._get_code_segment(init["actual_start_line"], init["end_line"])
                
                # Add line numbers to the init method
                init_lines = init_code.split('\n')
                numbered_init_code = '\n'.join(f"{init['actual_start_line'] + i}: {line}" 
                                            for i, line in enumerate(init_lines))
                
                init_info = {
                    "name": "__init__",
                    "params": ", ".join(init["params"]),
                    "line_number": init["start_line"],
                    "actual_start_line": init["actual_start_line"],
                    "end_line": init["end_line"],
                    "decorators": init.get("decorators", []),
                    "docstring": init.get("docstring"),
                    "header_comments": init.get("header_comments", []),
                    "numbered_code": numbered_init_code,
                    "code": init_code
                }
            
            # Build the complete class information text (including class definition and init method)
            complete_class_text = class_definition
            if init_code:
                # Ensure the indentation of the init method is correct
                indented_init_code = '\n'.join(f"{line}" for line in init_code.split('\n'))
                complete_class_text += f"\n\n{indented_init_code}"
            
            # Build the complete class information
            result["class_info"] = {
                "name": class_info["name"],
                "line_number": class_info["start_line"],
                "end_line": class_info["end_line"],
                "decorators": class_info.get("decorators", []),
                "docstring": class_info.get("docstring"),
                "header_comments": class_info.get("header_comments", []),
                "definition": class_definition,
                "numbered_definition": numbered_class_definition,
                "init_method": init_info,
                # 提供一个完整的类文本，包含所有重要元素并保持正确缩进
                "complete_info": complete_class_text
            }
        
        return result

    def _get_code_segment(self, start_line: int, end_line: int) -> str:
        """Get the code segment within the specified line range"""
        lines = self.module_code.split('\n')
        if start_line <= len(lines):
            if end_line > len(lines):
                end_line = len(lines)
            return '\n'.join(lines[start_line-1:end_line])
        return ""

    def _get_test_case_code(self, test_case, project_dir):
        """Get the test case code (including import statements, class definitions and test methods)"""
        module_name = test_case.get('module', '')
        module_path = f"{module_name.replace('.', '/')}.py"
        module_path = project_dir / module_path
        
        project_dir_str = str(project_dir)
        if project_dir_str not in sys.path:
            sys.path.insert(0, project_dir_str)  # 临时添加，避免影响全局

        try:
            rel_path = module_path.relative_to(project_dir)
            module_import_path = str(rel_path.with_suffix('')).replace('/', '.')
            
            class_name = test_case.get('class', '')
            method_name = test_case.get('method', '')
            
            # Import the module
            module = importlib.import_module(module_import_path)
            module_source = inspect.getsource(module)  # Get the source code of the entire module
            
            # Extract the import statements from the module
            import_statements = self._extract_imports(module_source)
            
            if class_name:
                # If the test method belongs to a class, extract the complete class definition
                test_class = getattr(module, class_name)
                class_source = inspect.getsource(test_class)
                
                # Combine: import statements + class definition
                full_code = import_statements + "\n\n" + class_source
            else:
                # If it is an independent function, directly extract the function code
                test_function = getattr(module, method_name)
                function_source = inspect.getsource(test_function)
                full_code = import_statements + "\n\n" + function_source
            
            return full_code
        except Exception as e:
            raise RuntimeError(f"Error retrieving test case code: {str(e)}")
        finally:
            # Restore sys.path (to avoid polluting subsequent imports)
            if project_dir_str in sys.path:
                sys.path.remove(project_dir_str)

    def _extract_imports(self, source_code):
        """Extract all import statements from the source code"""
        import_lines = []
        tree = ast.parse(source_code)
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                import_lines.append(ast.unparse(node))
        
        return "\n".join(import_lines)

    def _format_variable_state(self, variable_state):
        """Format the variable state as a readable string"""
        result = []
        for var_name, var_value in variable_state.items():
            if var_name == 'self':
                # Try to extract useful information from the self object
                try:
                    # If it is a string representation, try to extract the key attributes
                    if hasattr(var_value, '__dict__'):  # Check if it is an object
                        attrs = {k: v for k, v in var_value.__dict__.items() 
             if v not in ({}, [], False, None)}
                        import re
                        matches = re.findall(r'(\w+)=([^,}]+)', var_value)
                        for attr, val in matches:
                            if val != '{}' and val != '[]' and val != 'False' and val != 'None':
                                attrs[attr] = val
                        
                        if attrs:
                            result.append(f"self: Parser object with important attributes:")
                            for attr, val in attrs.items():
                                result.append(f"  - self.{attr} = {val}")
                        else:
                            result.append(f"self: {var_value}")
                    else:
                        result.append(f"self: {var_value}")
                except:
                    result.append(f"self: {var_value}")
            else:
                # Process the ordinary variables
                result.append(f"{var_name} = {var_value}")

        return "\n".join(result)

    def run_test_case(self, test_code: str, project_dir: str, test_dir: str) -> dict:
        """
        Create a temporary test file in the project directory, run the test case, and capture the running result and coverage
        """
        import unittest, io, json, importlib.util, time
        from contextlib import redirect_stdout, redirect_stderr

        print("\n" + "-"*40 + " Run the test case " + "-"*40)
        original_cwd = os.getcwd()
        os.chdir(project_dir)

        stdout_buffer = io.StringIO()
        stderr_buffer = io.StringIO()
        report_path = None
        temp_file_path = None
        test_result = {
            'test case': '',
            'success': False,
            'error': None,
            'output': '',
            'coverage': {},
            'coverage_percentage': 0.0
        }

        try:
            # Create a temporary test file
            with tempfile.NamedTemporaryFile(suffix='.py', dir=test_dir, delete=False) as temp_file:
                temp_file_path = temp_file.name
                print(f"Create a temporary test file: {os.path.basename(temp_file_path)}")

                # Construct the import statements
                from ImportGenerator import ImportGenerator
                importGenerator = ImportGenerator(test_dir)
                unique_imports = importGenerator.process_test_files()
                
                import_lines = [f"import sys\nsys.path.insert(0, '{project_dir}')", "import unittest", "import timeout_decorator"]
                import_lines += [imp for imp in unique_imports if imp.strip()]
                import_block = "\n".join(set(import_lines)) + "\n"

                # Write the test code
                full_code = import_block + test_code
                print(f"The complete test code generated:")
                print("-" * 80)
                print(full_code)
                print("-" * 80)
                temp_file.write(full_code.encode('utf-8'))
                test_result['test case'] = full_code
                temp_file.flush()
                os.fsync(temp_file.fileno())
            
            # Configure coverage collection
            source_path = os.path.dirname(os.path.abspath(self.target_module_path))
            data_file = os.path.join(self.module_dir, '.coverage')
            
            if not os.path.exists(self.target_module_path):
                print(f"Error: The target module file does not exist: {self.target_module_path}")
            
            # Create the coverage object
            self.cov = coverage.Coverage(
                source=[os.path.dirname(self.target_module_path)],
                data_file=data_file,
                omit=[
                    "*/tmp*.py",
                    "*/__pycache__/*",
                    "*/template*",
                ]
            )

            # Start collecting coverage
            self.cov.start()

            # Import the target module
            module_name = os.path.basename(self.target_module_path).replace('.py', '')
            module_dir = os.path.dirname(self.target_module_path)
            
            try:
                sys.path.insert(0, module_dir)
                module = __import__(module_name)
            except ImportError as e:
                print(f"Warning: Failed to import the module: {e}")

            # Execute the test
            try:
                with redirect_stdout(stdout_buffer), redirect_stderr(stderr_buffer):
                    test_module_name = os.path.basename(temp_file_path).replace('.py', '')
                    temp_dir = os.path.dirname(temp_file_path)
                    
                    sys.path.insert(0, temp_dir)
                    if project_dir not in sys.path:
                        sys.path.insert(1, project_dir)
                    
                    spec = importlib.util.spec_from_file_location(test_module_name, temp_file_path)
                    if spec is None:
                        print(f"Error: Failed to create the module specification")
                    else:
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)
                        
                        test_suite = unittest.TestLoader().loadTestsFromModule(module)
                        print(f"Found {test_suite.countTestCases()} test cases")
                        
                        result_obj = unittest.TextTestRunner(stream=stdout_buffer).run(test_suite)
                        test_result['success'] = result_obj.wasSuccessful()
                        
                        if not test_result['success']:
                            if result_obj.errors:
                                print(f"Test errors:")
                                for test, error in result_obj.errors:
                                    print(f"  - {test}: {error[:200]}...")
                            if result_obj.failures:
                                print(f"Test failures:")
                                for test, failure in result_obj.failures:
                                    print(f"  - {test}: {failure[:200]}...")

            except Exception as e:
                test_result['error'] = str(e)
                print(f"Error occurred while executing the test: {str(e)}")
                traceback.print_exc()

            finally:
                if temp_dir in sys.path:
                    sys.path.remove(temp_dir)
                
                    # Stop collecting coverage
                self.cov.stop()
                self.cov.save()

            # Generate the coverage report
            with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as report_file:
                report_path = report_file.name

            try:
                self.cov.json_report(outfile=report_path)
                
                with open(report_path, 'r') as f:
                    coverage_report = json.load(f)
            except Exception as e:
                print(f"Error occurred while generating or reading the coverage report: {str(e)}")
                coverage_report = {"files": {}}

            # Extract the coverage of the target module
            target_file = self.target_module_path
            file_data = None

            if target_file in coverage_report['files']:
                file_data = coverage_report['files'][target_file]
            else:
                for file_path in coverage_report['files']:
                    if os.path.basename(file_path) == os.path.basename(target_file):
                        file_data = coverage_report['files'][file_path]
                        break

            if file_data:
                executed = file_data.get('executed_lines', [])
                missing = file_data.get('missing_lines', [])
                total = len(executed) + len(missing)
                
                print(f"Coverage statistics: {len(executed)} lines executed, {len(missing)} lines not executed, total {total} lines")
                
                if total > 0:
                    coverage_pct = (len(executed) / total) * 100
                    test_result['coverage_percentage'] = coverage_pct
                    print(f"Coverage percentage: {coverage_pct:.2f}%")

                test_result['coverage'] = {
                    'covered_lines': executed,
                    'missing_lines': missing,
                    'total_lines': total
                }
            else:
                print(f"Unable to locate the coverage data of the target module: {os.path.basename(target_file)}")

        except Exception as e:
            test_result['error'] = str(e)
            print(f"Exception occurred during execution: {str(e)}")
            traceback.print_exc()

        finally:
            # Clean up temporary resources
            time.sleep(0.5)
            
            for path in [temp_file_path, report_path]:
                try:
                    if path and os.path.exists(path):
                        os.unlink(path)
                except Exception as e:
                    print(f"Failed to delete the temporary file: {os.path.basename(path)} -> {e}")

            # Delete the __pycache__ and .pyc files
            try:
                if temp_file_path:
                    pyc_path = temp_file_path.replace('.py', '.pyc')
                    if os.path.exists(pyc_path):
                        os.unlink(pyc_path)

                    pycache_dir = os.path.join(os.path.dirname(temp_file_path), '__pycache__')
                    if os.path.exists(pycache_dir):
                        name_prefix = os.path.basename(temp_file_path).replace('.py', '')
                        for f in os.listdir(pycache_dir):
                            if f.startswith(name_prefix):
                                os.unlink(os.path.join(pycache_dir, f))
            except Exception:
                pass

            # Clear the coverage data
            self.cov.erase()

        # Get the test output
        stdout_content = stdout_buffer.getvalue()
        stderr_content = stderr_buffer.getvalue()
        test_result['output'] = stdout_content + stderr_content
        
        if stderr_content:
            print(f"Test error output: {stderr_content[:200]}...")
        
        print(f"Test execution {'success' if test_result['success'] else 'failed'}, coverage: {test_result.get('coverage_percentage', 0):.2f}%")
        print("-"*80)
        
        os.chdir(original_cwd)
        return test_result


# if __name__ == '__main__':
#     llmgenerator = LLMTestGenerator(api_key="sk-gezc2Cl34rItfmUjsWbxM6ds83KE1hlJxiVkIaFLCuJLJapw", target_module_path="/data/zhuxx/TIARA-study/TIARA-test/test-apps/codetiming/codetiming/_timer.py")
#     group_list = llmgenerator.parse_line_numbers_from_similarity_json("/data/zhuxx/TIARA-study/TIARA-test/test-apps/codetiming/test_results/similarity_analysis.json","_timer.py")
#     project_dir = Path("/data/zhuxx/TIARA-study/TIARA-test/test-apps/codetiming")
#     test_dir = Path("/data/zhuxx/TIARA-study/TIARA-test/test-apps/codetiming/prepare_tests")
#     # print(str(group_list))
    
#     # 创建输出目录（如果不存在）
#     output_dir = "/data/zhuxx/TIARA-study/TIARA-test/test-apps/codetiming/generate_tests"
#     os.makedirs(output_dir, exist_ok=True)
#     target_root = os.path.abspath('/data/zhuxx/TIARA-study/TIARA-test/test-apps/codetiming')   # <- 改成你的根目
#     if target_root not in sys.path:
#         sys.path.insert(0, target_root)   
#     # 打开文件准备逐行写入
#     output_file = os.path.join(output_dir, "all_generation_records_parser.jsonl")
#     llmgenerator.coverage_trace_log_path = os.path.join(output_dir,"tiara_llm_call_vs_coverage.jsonl")
#     # 处理每个组并立即写入结果
#     for i, group in enumerate(group_list):
#         print("The current group is " + str(group))
#         currentrecord = llmgenerator.generate_tests(group, project_dir, test_dir, output_dir, 3)
        
#         # 将当前记录写入文件
#         with open(output_file, 'a', encoding='utf-8') as f:
#             # 写入JSON行
#             json_line = json.dumps(currentrecord, ensure_ascii=False)
#             f.write(json_line + '\n')
            
#         print(f"已完成组 {i+1}/{len(group_list)} 的测试生成并保存")
    
#     print(f"所有测试生成完成，结果已保存到 {output_file}")

#     try:
#             sys.path.remove(target_root)
#     except ValueError:
#             pass
        
## Test for extract_context_by_line
if __name__ == "__main__":
    parser = LLMTestGenerator(api_key="your_api_key", target_module_path="/path/to/project/target_module.py")
    line_number = your_line_number
    context = parser.extract_context_by_line(line_number)
    output_path = "/path/to/project/context_output.json"   # <- change to your output path
#     with open(output_path, "w", encoding="utf-8") as f:
#         json.dump(context, f, ensure_ascii=False, indent=2)
#     print(f"[INFO] Context saved to {output_path}")
