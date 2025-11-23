import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_49(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_48(self):
        try:
            str_0 = '4A/81C"Fw!:)/5n\r'
            int_0 = 4
            list_0 = [str_0, str_0, int_0, int_0]
            bool_0 = False
            filter_module_0 = module_0.FilterModule()
            str_1 = '2W{*\x0bzI@P-G!CWwV'
            var_0 = module_0.rand(int_0, list_0, bool_0, filter_module_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
