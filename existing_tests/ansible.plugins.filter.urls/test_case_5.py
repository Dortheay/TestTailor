import unittest
import timeout_decorator
import ansible.plugins.filter.urls as module_0

class Test_Urls_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = False
            var_0 = module_0.do_urlencode(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
