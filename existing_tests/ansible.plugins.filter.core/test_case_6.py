import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'V8y}+0'
            filter_module_0 = module_0.FilterModule()
            var_0 = module_0.regex_escape(filter_module_0)
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
            list_0 = [dict_0, dict_0]
            var_1 = module_0.subelements(dict_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
