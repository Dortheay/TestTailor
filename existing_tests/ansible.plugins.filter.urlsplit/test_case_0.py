import unittest
import timeout_decorator
import ansible.plugins.filter.urlsplit as module_0

class Test_Urlsplit_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '5'
            var_0 = module_0.split_url(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
