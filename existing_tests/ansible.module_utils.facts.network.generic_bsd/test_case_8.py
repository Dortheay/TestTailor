import unittest
import timeout_decorator
import ansible.module_utils.facts.network.generic_bsd as module_0

class Test_Generic_bsd_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = -1829
            bool_0 = True
            bool_1 = None
            float_0 = 3209.771238
            set_0 = {float_0, float_0, float_0, float_0}
            generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(set_0)
            var_0 = generic_bsd_ifconfig_network_0.parse_ether_line(int_0, bool_0, bool_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
