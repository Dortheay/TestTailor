import unittest
import timeout_decorator
import semantic_release.hvcs as module_0

class Test_Hvcs_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        optional_0 = module_0.get_token()
        optional_1 = module_0.get_token()
        github_0 = module_0.Github()
        gitlab_0 = module_0.Gitlab()
        optional_2 = gitlab_0.token()
        str_0 = github_0.domain()

if __name__ == "__main__":
    unittest.main()
