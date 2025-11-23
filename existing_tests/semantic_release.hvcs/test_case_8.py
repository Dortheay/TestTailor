import unittest
import timeout_decorator
import semantic_release.hvcs as module_0
import urllib3.util.retry as module_1

class Test_Hvcs_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            github_0 = module_0.Github()
            str_0 = github_0.api_url()
            str_1 = 'ozd\n-k\trQE'
            optional_0 = github_0.token()
            bool_0 = module_0.check_build_status(str_1, str_1, str_1)
            base_0 = module_0.get_hvcs()
            str_2 = base_0.domain()
            gitlab_0 = module_0.Gitlab()
            str_3 = github_0.domain()
            optional_1 = gitlab_0.token()
            str_4 = base_0.domain()
            optional_2 = base_0.token()
            base_1 = module_0.get_hvcs()
            str_5 = ':VVf2"0'
            base_2 = module_0.Base()
            bool_1 = base_2.check_build_status(str_0, str_0, str_5)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
