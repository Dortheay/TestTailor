import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_34(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_24(self):
        try:
            str_0 = 'wait'
            str_1 = 'protocol'
            str_2 = 'source'
            str_3 = 'destination'
            str_4 = 'match'
            str_5 = 'tcp_flags'
            str_6 = 'jump'
            str_7 = 'log_prefix'
            str_8 = 'log_level'
            str_9 = 'to_destination'
            str_10 = 'destination_ports'
            str_11 = 'to_source'
            str_12 = 'goto'
            str_13 = 'in_interface'
            str_14 = 'fragment'
            str_15 = 'set_counters'
            str_16 = 'source_port'
            str_17 = 'destination_port'
            str_18 = 'to_ports'
            str_19 = 'set_dscp_mark'
            str_20 = 'set_dscp_mark_class'
            str_21 = 'syn'
            str_22 = 'ctstate'
            str_23 = 'src_range'
            str_24 = 'dst_range'
            str_25 = 'match_set'
            str_26 = 'match_set_flags'
            str_27 = 'limit'
            str_28 = 'limit_burst'
            str_29 = 'uid_owner'
            str_30 = 'gid_owner'
            str_31 = 'reject_with'
            str_32 = 'icmp_type'
            str_33 = 'ip_version'
            str_34 = 'comment'
            str_35 = '2'
            str_36 = 'tcp'
            str_37 = '192.168.1.1'
            str_38 = '10.0.0.1'
            str_39 = 'flags'
            str_40 = 'flags_set'
            str_41 = 'ACK'
            str_42 = 'RST'
            str_43 = [str_41, str_42]
            str_44 = {str_39: str_3, str_40: str_43}
            str_45 = 'ACCEPT'
            var_0 = None
            str_46 = '80'
            str_47 = '443'
            str_48 = [str_46, str_47]
            str_49 = 'eth0'
            str_50 = 'ipv4'
            str_51 = 'Test rule'
            var_1 = {str_0: str_35, str_1: str_36, str_2: str_37, str_3: str_38, str_4: str_32, str_5: str_44, str_6: str_45, str_7: str_17, str_8: str_6, str_9: var_0, str_10: str_48, str_11: var_0, str_12: var_0, str_13: str_49, str_6: var_0, str_14: var_0, str_15: var_0, str_16: var_0, str_17: str_46, str_18: var_0, str_19: var_0, str_20: var_0, str_21: str_4, str_22: str_44, str_23: var_0, str_24: var_0, str_25: var_0, str_26: var_0, str_27: var_0, str_28: var_0, str_29: var_0, str_30: var_0, str_31: var_0, str_32: var_0, str_33: str_50, str_34: str_51}
            var_2 = module_0.construct_rule(var_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
