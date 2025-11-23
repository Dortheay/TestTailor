import unittest
import timeout_decorator
import ansible.module_utils.facts.network.generic_bsd as module_0

class Test_Generic_bsd_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            int_0 = -206
            set_0 = {int_0}
            list_0 = []
            generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(set_0, list_0)
            str_0 = 'full-upgrade'
            generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_0, generic_bsd_ifconfig_network_0)
            var_0 = generic_bsd_ifconfig_network_1.parse_inet_line(str_0, str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
