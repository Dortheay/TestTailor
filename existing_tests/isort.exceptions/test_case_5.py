import unittest
import timeout_decorator
import isort.exceptions as module_0
import builtins as module_1
import pathlib as module_2

class Test_Exceptions_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'skip_file'
        formatting_plugin_does_not_exist_0 = module_0.FormattingPluginDoesNotExist(str_0)

if __name__ == "__main__":
    unittest.main()
