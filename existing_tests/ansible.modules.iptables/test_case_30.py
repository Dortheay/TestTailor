import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
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
            str_14 = 'out_interface'
            str_15 = 'fragment'
            str_16 = 'set_counters'
            str_17 = 'source_port'
            str_18 = 'destination_port'
            str_19 = 'to_ports'
            str_20 = 'set_dscp_mark'
            str_21 = 'set_dscp_mark_class'
            str_22 = 'syn'
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
            str_39 = 'state'
            str_40 = [str_39]
            str_41 = 'flags'
            str_42 = 'flags_set'
            str_43 = [str_30]
            str_44 = 'ACK'
            str_45 = 'RST'
            str_46 = [str_44, str_45]
            str_47 = {str_41: str_43, str_42: str_46}
            str_48 = 'LOG:'
            str_49 = 'info'
            str_50 = '80'
            str_51 = '443'
            str_52 = [str_50, str_51]
            str_53 = 'eth0'
            str_54 = 'NEW'
            str_55 = 'ipv4'
            str_56 = 'Test rule'
            var_0 = {str_0: str_35, str_1: str_36, str_2: str_37, str_3: str_38, str_4: str_40, str_5: str_47, str_6: str_45, str_7: str_48, str_8: str_49, str_9: str_15, str_10: str_52, str_11: str_15, str_12: str_15, str_13: str_53, str_14: str_15, str_15: str_15, str_16: str_15, str_17: str_15, str_18: str_50, str_19: str_15, str_20: str_15, str_21: str_15, str_22: str_4, str_22: str_54, str_23: str_15, str_24: str_15, str_25: str_15, str_26: str_15, str_27: str_15, str_28: str_15, str_29: str_15, str_30: str_15, str_31: str_15, str_32: str_15, str_33: str_55, str_34: str_56}
            var_1 = module_0.construct_rule(var_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
