import unittest
import timeout_decorator
import isort.exceptions as module_0
import builtins as module_1
import pathlib as module_2

class Test_Exceptions_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'J6Y,\nud\r/o3'
        invalid_settings_path_0 = module_0.InvalidSettingsPath(str_0)

if __name__ == "__main__":
    unittest.main()
