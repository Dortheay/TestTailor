import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            bool_0 = True
            var_0 = module_0.generic_urlparse(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
