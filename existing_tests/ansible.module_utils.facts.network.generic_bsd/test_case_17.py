import unittest
import timeout_decorator
import ansible.module_utils.facts.network.generic_bsd as module_0

class Test_Generic_bsd_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            str_0 = 'bright purple'
            generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
            list_0 = [str_0, str_0, str_0]
            str_1 = "99',d)Xi6D|Y\nUJs<#"
            var_0 = generic_bsd_ifconfig_network_0.merge_default_interface(str_0, list_0, str_1)
            bool_0 = False
            generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(bool_0)
            set_0 = {bool_0, generic_bsd_ifconfig_network_1, str_0}
            bytes_0 = b''
            set_1 = set()
            var_1 = generic_bsd_ifconfig_network_0.parse_inet6_line(set_0, bytes_0, set_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
