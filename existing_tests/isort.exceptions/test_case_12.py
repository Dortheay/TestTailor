import unittest
import timeout_decorator
import isort.exceptions as module_0

class Test_Exceptions_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'M\x0bo0'
            str_1 = 'on'
            dict_0 = {str_0: str_1}
            str_2 = None
            dict_1 = {str_0: dict_0, str_2: dict_0}
            unsupported_settings_0 = module_0.UnsupportedSettings(dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
