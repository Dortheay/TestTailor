import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_41(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_40(self):
        try:
            list_0 = []
            request_0 = module_0.Request(list_0)
            bool_0 = False
            var_0 = request_0.head(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
