import unittest
import timeout_decorator
import ansible.module_utils.facts.network.generic_bsd as module_0

class Test_Generic_bsd_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            int_0 = -205
            set_0 = {int_0}
            list_0 = []
            str_0 = 'J|<oG/'
            bytes_0 = b'\x1d\x89~'
            str_1 = 'IByBbFKU;k(/F31~DHN'
            str_2 = 'h-1OxWI!)?/U9'
            tuple_0 = (bytes_0, list_0, str_1, str_2)
            generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(tuple_0)
            var_0 = generic_bsd_ifconfig_network_0.get_options(str_0)
            generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(set_0, list_0)
            float_0 = -4941.73
            bool_0 = True
            str_3 = "Rye'vO\nb5r"
            generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_1)
            var_1 = generic_bsd_ifconfig_network_2.parse_options_line(float_0, bool_0, str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
