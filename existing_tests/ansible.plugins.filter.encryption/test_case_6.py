import unittest
import timeout_decorator
import ansible.plugins.filter.encryption as module_0
import ansible.module_utils.common.text.converters as module_1
import ansible.parsing.vault as module_2
import ansible.parsing.yaml.objects as module_3

class Test_Encryption_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            complex_0 = None
            float_0 = 5589.3724
            filter_module_0 = module_0.FilterModule()
            var_0 = filter_module_0.filters()
            var_1 = module_0.do_unvault(complex_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
