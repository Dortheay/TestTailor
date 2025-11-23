import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        try:
            str_0 = 'protocol'
            str_1 = 'source'
            str_2 = 'destination'
            str_3 = 'jump'
            str_4 = 'wait'
            str_5 = 'match'
            str_6 = 'tcp_flags'
            str_7 = 'destination_ports'
            str_8 = 'ctstate'
            str_9 = 'src_range'
            str_10 = 'dst_range'
            str_11 = 'match_set'
            str_12 = 'match_set_flags'
            str_13 = 'limit'
            str_14 = 'limit_burst'
            str_15 = 'uid_owner'
            str_16 = 'gid_owner'
            str_17 = 'reject_with'
            str_18 = 'icmp_type'
            str_19 = 'ip_version'
            str_20 = 'comment'
            str_21 = 'tcp'
            str_22 = '192.168.1.1'
            str_23 = '192.168.1.2'
            str_24 = '5'
            var_0 = None
            str_25 = 'ipv4'
            var_1 = {str_0: str_21, str_1: str_22, str_2: str_23, str_3: str_7, str_4: str_24, str_5: str_21, str_6: var_0, str_7: var_0, str_8: var_0, str_9: var_0, str_10: var_0, str_11: var_0, str_12: var_0, str_13: var_0, str_14: var_0, str_15: var_0, str_16: var_0, str_17: var_0, str_18: var_0, str_19: str_25, str_20: var_0}
            var_2 = module_0.construct_rule(var_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
