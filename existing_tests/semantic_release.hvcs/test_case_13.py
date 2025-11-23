import unittest
import timeout_decorator
import semantic_release.hvcs as module_0
import urllib3.util.retry as module_1

class Test_Hvcs_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'O'
            str_1 = "B'%Y Nx"
            bool_0 = module_0.check_build_status(str_0, str_1, str_1)
            optional_0 = module_0.get_domain()
            base_0 = module_0.get_hvcs()
            str_2 = base_0.api_url()
            gitlab_0 = module_0.Gitlab()
            str_3 = '}ua5u6&V\r%'
            optional_1 = base_0.token()
            bool_1 = gitlab_0.check_build_status(str_0, str_0, str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
