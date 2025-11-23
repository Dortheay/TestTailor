import unittest
import timeout_decorator
import semantic_release.hvcs as module_0

class Test_Hvcs_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        list_0 = None
        str_0 = '4K1d\x0bQo'
        github_0 = module_0.Github()
        optional_0 = github_0.token()
        float_0 = 1482.627843
        dict_0 = {str_0: str_0, float_0: float_0}
        token_auth_0 = module_0.TokenAuth(dict_0)
        var_0 = token_auth_0.__eq__(list_0)

if __name__ == "__main__":
    unittest.main()
