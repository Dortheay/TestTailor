import unittest
import timeout_decorator
import semantic_release.hvcs as module_0
import urllib3.util.retry as module_1

class Test_Hvcs_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = '**[See all commits in this version]('
            bool_0 = True
            str_1 = 'Fz+,tUuLdOBN$Amo3(*'
            str_2 = 'J;VP}41x'
            str_3 = '[N(kJN'
            dict_0 = {str_3: str_2}
            dict_1 = {str_0: bool_0, str_1: str_1, str_2: bool_0, str_0: dict_0}
            float_0 = -2105.08307
            token_auth_0 = module_0.TokenAuth(float_0)
            var_0 = token_auth_0.__call__(dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
