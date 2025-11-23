import unittest
import timeout_decorator
import semantic_release.hvcs as module_0
import urllib3.util.retry as module_1

class Test_Hvcs_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            bool_0 = True
            optional_0 = module_0.get_domain()
            base_0 = module_0.get_hvcs()
            str_0 = 'Vn\t@PK%U6j'
            str_1 = 'e<5i7&#KyFr$]DNz'
            bool_1 = base_0.check_build_status(str_0, str_0, str_1)
            optional_1 = module_0.get_domain()
            str_2 = base_0.domain()
            optional_2 = module_0.get_token()
            list_0 = [bool_0, bool_0]
            gitlab_0 = module_0.Gitlab(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
