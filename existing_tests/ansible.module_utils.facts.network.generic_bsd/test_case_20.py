import unittest
import timeout_decorator
import ansible.module_utils.facts.network.generic_bsd as module_0

class Test_Generic_bsd_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            bool_0 = False
            int_0 = -4297
            generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0, int_0)
            tuple_0 = ()
            var_0 = generic_bsd_ifconfig_network_0.detect_type_media(tuple_0)
            str_0 = '\r"?#Z=aA'
            var_1 = generic_bsd_ifconfig_network_0.parse_interface_line(str_0)
            var_2 = generic_bsd_ifconfig_network_0.get_default_interfaces(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
