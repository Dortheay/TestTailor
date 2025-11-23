import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            float_0 = 1530.47444
            list_0 = []
            float_1 = 1000.0
            int_0 = 2116
            var_0 = module_0.append_wait(list_0, float_1, int_0)
            bytes_0 = b'\xc6\x8e\xabK\xfa\xcbp\xa5IX'
            bool_0 = True
            str_0 = '>_)\r8<I\'Qw[\\\\&K"u ?['
            var_1 = module_0.append_match_flag(float_0, bytes_0, bool_0, str_0)
            str_1 = 'yM\x0bo`_i7&yC'
            list_1 = []
            str_2 = ''
            var_2 = module_0.flush_table(str_1, list_1, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
