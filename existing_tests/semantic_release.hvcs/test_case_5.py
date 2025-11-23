import unittest
import timeout_decorator
import semantic_release.hvcs as module_0

class Test_Hvcs_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        optional_0 = module_0.get_domain()
        github_0 = module_0.Github()
        str_0 = github_0.api_url()
        token_auth_0 = None
        optional_1 = module_0.get_domain()
        session_0 = github_0.session()
        token_auth_1 = module_0.TokenAuth(token_auth_0)
        var_0 = token_auth_1.__call__(session_0)
        str_1 = '`|73'
        token_auth_2 = module_0.TokenAuth(str_1)
        var_1 = token_auth_1.__call__(session_0)

if __name__ == "__main__":
    unittest.main()
