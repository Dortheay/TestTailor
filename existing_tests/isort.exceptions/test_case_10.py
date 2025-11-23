import unittest
import timeout_decorator
import isort.exceptions as module_0
import builtins as module_1
import pathlib as module_2

class Test_Exceptions_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        str_0 = 'option1'
        str_1 = 'option2'
        str_2 = 'value'
        str_3 = 'source'
        str_4 = 'invalid_value'
        str_5 = 'config_file'
        str_6 = {str_2: str_4, str_3: str_5}
        str_7 = 'unsupported_value'
        str_8 = 'CLI'
        str_9 = {str_2: str_7, str_3: str_8}
        str_10 = {str_0: str_6, str_1: str_9}
        unsupported_settings_0 = module_0.UnsupportedSettings(str_10)
        var_0 = str(unsupported_settings_0)

if __name__ == "__main__":
    unittest.main()
