import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            int_0 = None
            float_0 = -18.55103704286351
            str_0 = 'gze'
            float_1 = -544.0
            dict_0 = {str_0: float_0, int_0: float_1}
            var_0 = module_0.append_match_flag(float_0, str_0, str_0, dict_0)
            float_2 = 2699.217
            bytes_0 = b'\x07\x12\x19s)\xd9\xffp\x9a\x9c&\xda\x0e\xb0\xc7\xeb\x82p\xbf'
            str_1 = 'l&1?W;N:b{w#"REW'
            tuple_0 = ()
            set_0 = None
            var_1 = module_0.append_param(tuple_0, int_0, set_0, tuple_0)
            set_1 = None
            var_2 = module_0.append_wait(str_1, set_1, int_0)
            var_3 = module_0.append_tcp_flags(float_2, dict_0, bytes_0)
            str_2 = '\th'
            var_4 = module_0.check_present(str_2, int_0, float_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
