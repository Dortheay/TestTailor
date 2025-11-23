import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_29(self):
        try:
            str_0 = None
            bool_0 = False
            var_0 = module_0.fetch_url(str_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
