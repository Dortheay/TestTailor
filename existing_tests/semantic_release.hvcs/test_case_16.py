import unittest
import timeout_decorator
import semantic_release.hvcs as module_0
import urllib3.util.retry as module_1

class Test_Hvcs_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            bool_0 = module_0.check_token()
            str_0 = '&f(0jB7)Bi@DJ!'
            str_1 = '"xd\'X7;r\\H$u'
            dict_0 = {str_1: str_1, str_1: str_0}
            base_0 = module_0.Base(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
