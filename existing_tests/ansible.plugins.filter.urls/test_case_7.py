import unittest
import timeout_decorator
import ansible.plugins.filter.urls as module_0

class Test_Urls_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            filter_module_0 = module_0.FilterModule()
            var_0 = filter_module_0.filters()
            dict_0 = {filter_module_0: filter_module_0, filter_module_0: var_0}
            var_1 = module_0.do_urlencode(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
