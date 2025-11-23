import unittest
import timeout_decorator
import httpie.utils as module_0

class Test_Utils_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'du[#r&i3/t5mn0?c'
            bool_0 = True
            var_0 = module_0.humanize_bytes(bool_0)
            explicit_null_auth_0 = module_0.ExplicitNullAuth()
            str_1 = ''
            str_2 = 'UbjU'
            dict_0 = {str_1: explicit_null_auth_0, str_1: str_0, str_2: str_1}
            var_1 = module_0.get_content_type(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
