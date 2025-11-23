import unittest
import timeout_decorator
import ansible.plugins.filter.urlsplit as module_0

class Test_Urlsplit_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            dict_0 = {}
            filter_module_0 = module_0.FilterModule()
            var_0 = filter_module_0.filters()
            float_0 = -13.137172600362389
            var_1 = module_0.split_url(dict_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
