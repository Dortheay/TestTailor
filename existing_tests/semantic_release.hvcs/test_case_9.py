import unittest
import timeout_decorator
import semantic_release.hvcs as module_0
import urllib3.util.retry as module_1

class Test_Hvcs_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            int_0 = 1976
            list_0 = [int_0, int_0, int_0, int_0]
            token_auth_0 = module_0.TokenAuth(list_0)
            str_0 = '~'
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
            base_0 = module_0.Base(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
