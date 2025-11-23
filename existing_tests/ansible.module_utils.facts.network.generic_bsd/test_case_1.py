import unittest
import timeout_decorator
import ansible.module_utils.facts.network.generic_bsd as module_0

class Test_Generic_bsd_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'a\x0cuZM"\x0c(/!i47'
        str_1 = 'KVM Server'
        int_0 = -1881
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_1, int_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(str_0)

if __name__ == "__main__":
    unittest.main()
