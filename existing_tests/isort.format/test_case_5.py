import unittest
import timeout_decorator
import isort.format as module_0
import pathlib as module_1

class Test_Format_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'Finds and returns all imports within the provided code stream.\n\n    - **input_stream**: The stream of code with imports that need to be sorted.\n    - **config**: The config object to use when sorting imports.\n    - **file_path**: The disk location where the code string was pulled from.\n    - **unique**: If True, only the first instance of an import is returned.\n    - **top_only**: If True, only return imports that occur before the first function or class.\n    - **_seen**: An optional set of imports already seen. Generally meant only for internal use.\n    - ****config_kwargs**: Any config modifications.\n    '
        basic_printer_0 = module_0.BasicPrinter()
        basic_printer_0.success(str_0)

if __name__ == "__main__":
    unittest.main()
