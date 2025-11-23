import unittest
import timeout_decorator
import ansible.module_utils.facts.network.generic_bsd as module_0

class Test_Generic_bsd_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            str_0 = 'U eHJ`Q\x0bs3Q8\x0b(3$WwN?'
            int_0 = 1890
            generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0)
            tuple_0 = ()
            list_0 = [int_0, tuple_0, str_0]
            float_0 = -625.16069
            var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(list_0, generic_bsd_ifconfig_network_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
