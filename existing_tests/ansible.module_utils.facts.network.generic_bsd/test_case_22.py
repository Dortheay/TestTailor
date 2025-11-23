import unittest
import timeout_decorator
import ansible.module_utils.facts.network.generic_bsd as module_0

class Test_Generic_bsd_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            bytes_0 = b'/\x1e\xb0\x96\x81ml\x80\xc3'
            complex_0 = None
            bool_0 = False
            str_0 = 'A&JS\n/Mh|'
            float_0 = -452.2017122613161
            dict_0 = {float_0: float_0, str_0: bytes_0, bytes_0: str_0, float_0: str_0}
            bool_1 = False
            generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_1)
            str_1 = '/g{1Q\\\te}LG>[.'
            list_0 = [dict_0, str_1, bool_0, dict_0]
            var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(list_0, generic_bsd_ifconfig_network_0, complex_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
