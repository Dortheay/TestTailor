import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        int_0 = None
        str_0 = ''
        float_0 = -544.0
        dict_0 = {str_0: float_0, int_0: float_0}
        var_0 = module_0.append_match_flag(float_0, str_0, str_0, dict_0)
        bytes_0 = b'\x07\x12\x19s)\xd9\xffp\x9a\x9c&\xda\x0e\xb0\xc7\xeb\x82p\xbf'
        str_1 = 'l&1?W;N:b{w#"REW'
        set_0 = None
        list_0 = []
        bool_0 = False
        str_2 = 'ansible.modules.iptables'
        var_1 = module_0.append_tcp_flags(list_0, bool_0, str_2)
        var_2 = module_0.append_wait(str_1, set_0, int_0)
        var_3 = module_0.append_tcp_flags(float_0, dict_0, bytes_0)
        var_4 = module_0.main()
        str_3 = 'ansible.modules.iptables'
        bool_1 = False
        var_5 = module_0.set_chain_policy(str_0, str_3, bool_1)

if __name__ == "__main__":
    unittest.main()
