import unittest
import timeout_decorator
import ansible.module_utils.facts.network.generic_bsd as module_0

class Test_Generic_bsd_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = '['
            bytes_0 = b'\xef\xb8\x19(5/a\x1f'
            list_0 = [bytes_0, bytes_0, str_0, bytes_0]
            set_0 = None
            tuple_0 = (str_0, bytes_0, list_0, set_0)
            dict_0 = {}
            bool_0 = False
            list_1 = [bool_0, bool_0, bool_0, bool_0]
            generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(list_1)
            var_0 = generic_bsd_ifconfig_network_0.parse_tunnel_line(tuple_0, list_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
