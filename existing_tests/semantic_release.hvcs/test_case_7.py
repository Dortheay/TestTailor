import unittest
import timeout_decorator
import semantic_release.hvcs as module_0
import urllib3.util.retry as module_1

class Test_Hvcs_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = None
            base_0 = module_0.get_hvcs()
            bool_0 = module_0.check_build_status(str_0, str_0, str_0)
            base_1 = module_0.Base()
            str_1 = base_1.api_url()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
