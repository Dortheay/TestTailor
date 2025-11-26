import os
import sys
import coverage
import json
import subprocess
import pytest
from typing import Dict, List, Any, Optional, Tuple
import datetime
import argparse

from python_code_structure_parser import PythonCodeParser, Node
from enhanced_python_analyzer import EnhancedPythonAnalyzer

class CoverageDataCollector:
    def __init__(self, src_dir: str, test_dir: str):
        self.src_dir = os.path.abspath(src_dir)
        self.test_dir = os.path.abspath(test_dir)
        
        self.project_root = os.path.dirname(self.src_dir)
        self.cov = coverage.Coverage(source=[src_dir])
    
    def run_tests_with_coverage(self) -> Dict[str, Any]:
        print(f"Project root: {self.project_root}")
        print(f"Source directory: {self.src_dir}")
        print(f"Test directory: {self.test_dir}")

        original_cwd = os.getcwd()
        original_sys_path = sys.path.copy()
        original_pythonpath = os.environ.get('PYTHONPATH', '')
        
        try:
            os.chdir(self.project_root)
            print(f"Changed directory to project root: {self.project_root}")

            new_pythonpath = self.project_root
            if original_pythonpath:
                new_pythonpath = f"{self.project_root}:{original_pythonpath}"
            os.environ['PYTHONPATH'] = new_pythonpath

            if self.project_root not in sys.path:
                sys.path.insert(0, self.project_root)
            
            print(f"PYTHONPATH set to: {new_pythonpath}")

            valid_test_files = self._filter_valid_test_files(self.test_dir)
            if not valid_test_files:
                print("Warning: No valid test files found")
                test_target = self.test_dir
            else:
                print(f"Found {len(valid_test_files)} valid test files")
                test_target = valid_test_files

            pytest_args = [
                *(test_target if isinstance(test_target, list) else [test_target]),
                f"--cov={self.src_dir}",
                "--cov-report=term-missing",
                "-v"
            ]

            try:
                import pytest_cov
                version = pytest_cov.__version__
                
                if hasattr(pytest_cov, 'REPORT_CHOICES') and 'json' in pytest_cov.REPORT_CHOICES:
                    pytest_args.append("--cov-report=json:coverage.json")
                else:
                    print("Notice: pytest-cov does not support JSON report")
            except (ImportError, AttributeError):
                print("Notice: pytest-cov does not support JSON report")
            
            print("Running pytest...")
            result = pytest.main(pytest_args)

            return self._load_coverage_data()
            
        finally:
            os.chdir(original_cwd)
            sys.path = original_sys_path
            if original_pythonpath:
                os.environ['PYTHONPATH'] = original_pythonpath
            else:
                os.environ.pop('PYTHONPATH', None)
            print(f"Restored working directory: {original_cwd}")

    def _filter_valid_test_files(self, test_dir: str) -> List[str]:
        valid_files = []

        if os.path.isfile(test_dir) and test_dir.endswith('.py'):
            if self._is_valid_python_file(test_dir):
                return [test_dir]
            else:
                return []

        for root, _, files in os.walk(test_dir):
            for file in files:
                if file.startswith('test_') and file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    if self._is_valid_python_file(file_path):
                        valid_files.append(file_path)
                    else:
                        print(f"Skipped invalid test file: {file_path}")
        
        return valid_files

    def _is_valid_python_file(self, file_path: str) -> bool:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                source = f.read()
            compile(source, file_path, 'exec')
            return True
        except SyntaxError as e:
            print(f"Syntax error ({file_path}:{e.lineno}): {e.msg}")
            return False
        except Exception as e:
            print(f"File error ({file_path}): {str(e)}")
            return False

    def _load_coverage_data(self) -> Dict[str, Any]:
        coverage_data = {}

        json_file = os.path.join(self.project_root, 'coverage.json')
        if os.path.exists(json_file):
            try:
                with open(json_file, 'r') as f:
                    json_data = json.load(f)
                coverage_data = self._parse_json_coverage(json_data)
                print(f"Loaded coverage data from {json_file}")
            except Exception as e:
                print(f"Failed to parse JSON coverage data: {e}")

        if not coverage_data:
            coverage_file = os.path.join(self.project_root, '.coverage')
            if os.path.exists(coverage_file):
                try:
                    temp_cov = coverage.Coverage(data_file=coverage_file)
                    temp_cov.load()
                    coverage_data = self._parse_coverage_object(temp_cov)
                    print(f"Loaded coverage data from {coverage_file}")
                except Exception as e:
                    print(f"Failed to parse .coverage file: {e}")
        
        if not coverage_data:
            print("Warning: No coverage data found")
        
        return coverage_data
    
    def _parse_json_coverage(self, json_data: Dict) -> Dict[str, Any]:
        coverage_data = {}
        files_data = json_data.get('files', {})
        for file_path, file_data in files_data.items():
            if self.src_dir in file_path and file_path.endswith('.py'):
                rel_path = os.path.relpath(file_path, self.src_dir)
                
                executed_lines = file_data.get('executed_lines', [])
                missing_lines = file_data.get('missing_lines', [])
                
                total_lines = len(executed_lines) + len(missing_lines)
                coverage_percent = 0
                if total_lines > 0:
                    coverage_percent = len(executed_lines) / total_lines * 100
                
                coverage_data[rel_path] = {
                    'covered_lines': sorted(executed_lines),
                    'missing_lines': sorted(missing_lines),
                    'coverage_percent': coverage_percent,
                    'total_lines': total_lines
                }
        
        return coverage_data
    
    def _parse_coverage_object(self, cov_obj: coverage.Coverage) -> Dict[str, Any]:
        coverage_data = {}
        data = cov_obj.get_data()
        for file_path in data.measured_files():
            if self.src_dir in file_path and file_path.endswith('.py'):
                rel_path = os.path.relpath(file_path, self.src_dir)
                covered_lines = list(data.lines(file_path))
                missing_lines = self._get_missing_lines(file_path, covered_lines)
                
                total_lines = len(covered_lines) + len(missing_lines)
                coverage_percent = 0
                if total_lines > 0:
                    coverage_percent = len(covered_lines) / total_lines * 100
                
                coverage_data[rel_path] = {
                    'covered_lines': sorted(covered_lines),
                    'missing_lines': sorted(missing_lines),
                    'coverage_percent': coverage_percent,
                    'total_lines': total_lines
                }
        
        return coverage_data
    
    def _get_missing_lines(self, file_path: str, covered_lines: List[int]) -> List[int]:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                source_code = f.read()

            parser = PythonCodeParser(source_code)

            executable_lines = set()
            for node in parser.node_map.values():
                if hasattr(node, 'is_actual_code') and node.is_actual_code:
                    if node.node_type not in ['function', 'class']:
                        executable_lines.add(node.line_number)

            missing_lines = sorted(executable_lines - set(covered_lines))
            return missing_lines
        
        except Exception as e:
            print(f"Failed to analyze executable lines for {file_path}: {e}")
            return []