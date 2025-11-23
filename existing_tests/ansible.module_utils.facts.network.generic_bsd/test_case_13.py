import unittest
import timeout_decorator
import ansible.module_utils.facts.network.generic_bsd as module_0

class Test_Generic_bsd_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            int_0 = 1110
            str_0 = 'J}Rp@'
            set_0 = {str_0}
            str_1 = 'Ra_%<'
            list_0 = [int_0]
            generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(list_0)
            var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(str_0, set_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
