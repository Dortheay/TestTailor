import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_48(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_47(self):
        try:
            str_0 = ' ,Q\t9fGj~+h~EP'
            int_0 = -4956
            filter_module_0 = module_0.FilterModule()
            str_1 = 'mr.VU@}'
            var_0 = module_0.regex_findall(int_0, filter_module_0, str_1, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
