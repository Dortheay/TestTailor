import unittest
import timeout_decorator
import ansible.module_utils.facts.network.generic_bsd as module_0

class Test_Generic_bsd_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'uDmH'
            generic_bsd_ifconfig_network_0 = None
            float_0 = None
            bool_0 = True
            generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(bool_0)
            var_0 = generic_bsd_ifconfig_network_1.parse_status_line(str_0, generic_bsd_ifconfig_network_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
