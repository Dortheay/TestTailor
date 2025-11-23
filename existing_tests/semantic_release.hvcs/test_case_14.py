import unittest
import timeout_decorator
import semantic_release.hvcs as module_0
import urllib3.util.retry as module_1

class Test_Hvcs_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            base_0 = module_0.get_hvcs()
            str_0 = 'O'
            str_1 = "B'%Y Nx"
            bool_0 = module_0.check_build_status(str_0, str_1, str_1)
            base_1 = module_0.get_hvcs()
            str_2 = base_1.api_url()
            gitlab_0 = module_0.Gitlab()
            str_3 = '}ua5u6&V\r%'
            optional_0 = base_1.token()
            optional_1 = module_0.get_domain()
            list_0 = [str_3, bool_0, str_2]
            github_0 = module_0.Github(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
