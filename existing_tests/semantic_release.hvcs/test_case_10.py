import unittest
import timeout_decorator
import semantic_release.hvcs as module_0
import urllib3.util.retry as module_1

class Test_Hvcs_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            gitlab_0 = None
            token_auth_0 = module_0.TokenAuth(gitlab_0)
            base_0 = module_0.get_hvcs()
            var_0 = token_auth_0.__ne__(base_0)
            var_1 = token_auth_0.__call__(base_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
