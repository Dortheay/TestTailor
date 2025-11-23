import unittest
import timeout_decorator
import ansible.plugins.filter.encryption as module_0
import ansible.module_utils.common.text.converters as module_1
import ansible.parsing.vault as module_2
import ansible.parsing.yaml.objects as module_3

class Test_Encryption_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            complex_0 = None
            float_0 = 5589.3724
            var_0 = module_0.do_unvault(complex_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
