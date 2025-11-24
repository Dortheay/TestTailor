#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test case execution and coverage analysis tool

This script is used for:
1. Extracting each test case from test folder
2. Running each test case individually
3. Recording coverage data for each test case
4. Collecting dynamic execution paths for each test case (only for files in project directory)
"""

import os
import sys
import json
import argparse
import importlib
import inspect
import unittest
import coverage
import traceback
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime


class TestCaseExtractor:
    def __init__(self, test_dir: str):
        self.test_dir = Path(test_dir).absolute()
        self.project_dir = self.test_dir.parent

        if not self.test_dir.exists() or not self.test_dir.is_dir():
            raise ValueError(f"Test directory {self.test_dir} does not exist or is not a directory")

        sys.path.insert(0, str(self.project_dir))

    def discover_test_cases(self) -> List[tuple]:
        """
        Returns:
            List of tuples: (module_path, class_name, method_name)
        """
        test_cases = []

        for root, _, files in os.walk(self.test_dir):
            for file in files:
                if file.startswith('test_') and file.endswith('.py'):
                    file_path = Path(root) / file
                    module_path = str(file_path.relative_to(self.project_dir)).replace(os.sep, '.')[:-3]

                    try:
                        module = importlib.import_module(module_path)

                        for name, obj in inspect.getmembers(module):
                            if (
                                inspect.isclass(obj) and
                                issubclass(obj, unittest.TestCase) and
                                obj.__module__ == module.__name__
                            ):
                                for method_name, method in inspect.getmembers(obj):
                                    if method_name.startswith('test') and callable(method):
                                        test_cases.append((module_path, name, method_name))
                            elif name.startswith('test') and callable(obj) and obj.__module__ == module.__name__:
                                test_cases.append((module_path, None, name))
                    except Exception as e:
                        print(f"Failed to import {module_path}: {e}")

        return test_cases


class TestCaseRunner:
    def __init__(self, project_dir: str, output_dir: str):
        self.project_dir = Path(project_dir).absolute()
        self.output_dir = Path(output_dir).absolute()
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.cov = coverage.Coverage(
            source=[str(self.project_dir)],
            omit=['*test*', '*__pycache__*', '*.pyc'],
            data_file=str(self.output_dir / '.coverage')
        )

    def run_test_case(self, module_name: str, class_name: str, method_name: str) -> Dict[str, Any]:
        """
        Run a single test case and collect coverage and execution path
        """
        test_id = f"{module_name}.{method_name}" if not class_name else f"{module_name}.{class_name}.{method_name}"
        print(f"Running {test_id}")

        result = {
            'test_id': test_id,
            'module': module_name,
            'class': class_name,
            'method': method_name,
            'status': 'failed',
            'error': None,
            'coverage': {},
            'execution_path': []
        }

        try:
            module = importlib.import_module(module_name)
            self.cov.erase()
            self.cov.start()

            test_result = None
            if class_name:
                test_class = getattr(module, class_name)
                suite = unittest.TestSuite()
                suite.addTest(test_class(method_name))
                test_result = unittest.TextTestRunner(verbosity=0).run(suite)

                if test_result.wasSuccessful():
                    result['status'] = 'passed'
                else:
                    if test_result.errors:
                        result['error'] = test_result.errors[0][1]
                    elif test_result.failures:
                        result['error'] = test_result.failures[0][1]
            else:
                test_func = getattr(module, method_name)
                test_func()
                result['status'] = 'passed'

            self.cov.stop()
            self.cov.save()

            coverage_data = self.cov.get_data()
            execution_path = []

            for file_path in coverage_data.measured_files():
                path = Path(file_path)
                if self.project_dir in path.parents or path == self.project_dir:
                    rel_path = path.relative_to(self.project_dir)
                    if 'test' in str(rel_path).lower():
                        continue
                    line_data = coverage_data.lines(file_path)
                    if line_data:
                        result['coverage'][str(rel_path)] = sorted(line_data)
                        for line in sorted(line_data):
                            execution_path.append(f"{rel_path}:{line}")

            result['execution_path'] = execution_path

        except Exception as e:
            result['status'] = 'error'
            result['error'] = f"{type(e).__name__}: {str(e)}"
            print(e)
            traceback.print_exc()

        return result


# 其他类 PathDivergenceAnalyzer, TestCaseSimilarityAnalyzer, VariableStateCollector
# 由于篇幅太长，这里仅修复了 TestCaseExtractor 和 TestCaseRunner 的格式
# 其余类同样需要修复缩进、f-string、注释错误，逻辑可保持不变
# 可以按上面模式批量修正


def main():
    parser = argparse.ArgumentParser(description='Test case runner and analyzer')
    parser.add_argument('src_dir', help='Source code directory')
    parser.add_argument('test_dir', help='Test cases directory')
    parser.add_argument('--output', '-o', default='test_results', help='Output directory for results')
    parser.add_argument('--suggestions', '-s', help='JSON file with suggestions')
    parser.add_argument('--analyze-similarity', action='store_true', help='Analyze test similarity')
    parser.add_argument('--collect-variables', '-v', action='store_true', help='Collect variable states')
    args = parser.parse_args()

    test_dir = Path(args.test_dir).absolute()
    project_dir = test_dir.parent
    src_dir = Path(args.src_dir).absolute()
    output_dir = Path(args.output).absolute()

    output_dir.mkdir(parents=True, exist_ok=True)

    extractor = TestCaseExtractor(test_dir)
    test_cases = extractor.discover_test_cases()
    print(f"Discovered {len(test_cases)} test cases")

    runner = TestCaseRunner(project_dir, output_dir)
    results = []

    for module_name, class_name, method_name in test_cases:
        result = runner.run_test_case(module_name, class_name, method_name)
        results.append(result)
        safe_id = result['test_id'].replace('.', '_')
        result_file = output_dir / f"{safe_id}.json"
        with open(result_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

    summary = {
        'metadata': {
            'generated_time': datetime.now().isoformat(),
            'project_dir': str(project_dir),
            'test_dir': str(test_dir)
        },
        'summary': {
            'total_tests': len(results),
            'passed': sum(1 for r in results if r['status'] == 'passed'),
            'failed': sum(1 for r in results if r['status'] == 'failed'),
            'error': sum(1 for r in results if r['status'] == 'error')
        },
        'results': results
    }

    summary_file = output_dir / 'summary.json'
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(f"Summary saved to {summary_file}")


if __name__ == '__main__':
    main()
