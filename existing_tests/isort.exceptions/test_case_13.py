import unittest
import timeout_decorator
import isort.exceptions as module_0

class Test_Exceptions_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'option1'
            str_1 = 'option2'
            str_2 = 'value'
            str_3 = 'source'
            str_4 = 'invalid_value'
            str_5 = 'config_file'
            str_6 = {str_2: str_4, str_3: str_5}
            str_7 = {str_0: str_6, str_1: str_1}
            unsupported_settings_0 = module_0.UnsupportedSettings(str_7)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
