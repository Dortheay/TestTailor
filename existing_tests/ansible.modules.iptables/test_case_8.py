import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
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
        str_23 = 'ctstate'
        str_24 = 'src_range'
        str_25 = 'dst_range'
        str_26 = 'match_set'
        str_27 = 'match_set_flags'
        str_28 = 'limit'
        str_29 = 'limit_burst'
        str_30 = 'uid_owner'
        str_31 = 'gid_owner'
        str_32 = 'reject_with'
        str_33 = 'icmp_type'
        str_34 = 'ip_version'
        str_35 = 'comment'
        str_36 = '2'
        str_37 = 'tcp'
        str_38 = '192.168.1.1'
        str_39 = 'flags'
        str_40 = 'flags_set'
        str_41 = 'RST'
        str_42 = [str_16, str_41]
        str_43 = {str_39: str_3, str_40: str_42}
        str_44 = 'ACCEPT'
        str_45 = '80'
        str_46 = [str_45, str_36]
        str_47 = 'ipv4'
        str_48 = 'Test rule'
        var_0 = {str_0: str_36, str_1: str_37, str_2: str_38, str_3: str_28, str_4: str_33, str_5: str_43, str_6: str_44, str_7: str_18, str_8: str_14, str_9: str_33, str_10: str_46, str_11: str_33, str_12: str_33, str_13: str_30, str_14: str_33, str_15: str_33, str_16: str_33, str_17: str_33, str_18: str_45, str_19: str_33, str_20: str_33, str_21: str_33, str_22: str_4, str_23: str_43, str_24: str_33, str_25: str_33, str_26: str_33, str_27: str_33, str_28: str_33, str_29: str_33, str_30: str_33, str_31: str_33, str_32: str_33, str_33: str_33, str_34: str_47, str_35: str_48}
        var_1 = module_0.construct_rule(var_0)

if __name__ == "__main__":
    unittest.main()
