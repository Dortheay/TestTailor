import unittest
import timeout_decorator
import semantic_release.hvcs as module_0
import urllib3.util.retry as module_1

class Test_Hvcs_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = ', status code: '
            github_0 = module_0.Github()
            str_1 = 'pyproject.toml'
            str_2 = 'aEf5:k/S\n\x0cCR'
            bool_0 = github_0.check_build_status(str_0, str_2, str_1)
            tuple_0 = ()
            set_0 = {tuple_0, str_1, str_1}
            list_0 = []
            gitlab_0 = module_0.Gitlab(*list_0)
            str_3 = gitlab_0.domain()
            retry_0 = module_1.Retry(github_0, tuple_0, set_0)
            session_0 = github_0.session(retry_0)
            optional_0 = github_0.auth()
            str_4 = github_0.api_url()
            gitlab_1 = module_0.Gitlab()
            str_5 = gitlab_1.domain()
            optional_1 = github_0.token()
            list_1 = []
            base_0 = module_0.Base(*list_1)
            str_6 = base_0.domain()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
