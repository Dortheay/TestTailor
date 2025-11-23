import unittest
import timeout_decorator
import ansible.module_utils.facts.network.generic_bsd as module_0

class Test_Generic_bsd_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'RM5CT\rQ'
            dict_0 = {str_0: str_0}
            tuple_0 = (str_0, dict_0, str_0)
            int_0 = -1207
            generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0)
            bool_0 = True
            int_1 = 3058
            generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(int_1)
            var_0 = generic_bsd_ifconfig_network_1.parse_media_line(tuple_0, generic_bsd_ifconfig_network_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
