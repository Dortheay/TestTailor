import unittest
import timeout_decorator
import ansible.module_utils.facts.network.generic_bsd as module_0

class Test_Generic_bsd_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bytes_0 = b'\x1d'
        tuple_0 = ()
        str_0 = 'I`u5B'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(tuple_0, str_0)
        str_1 = ''
        tuple_1 = None
        set_0 = set()
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(set_0)
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_1)
        tuple_2 = (tuple_1, generic_bsd_ifconfig_network_2)
        generic_bsd_ifconfig_network_3 = module_0.GenericBsdIfconfigNetwork(tuple_2)
        generic_bsd_ifconfig_network_4 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_3)
        var_0 = generic_bsd_ifconfig_network_4.parse_unknown_line(bytes_0, generic_bsd_ifconfig_network_0, str_1)

if __name__ == "__main__":
    unittest.main()
