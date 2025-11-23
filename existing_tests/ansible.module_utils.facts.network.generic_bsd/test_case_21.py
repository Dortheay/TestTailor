import unittest
import timeout_decorator
import ansible.module_utils.facts.network.generic_bsd as module_0

class Test_Generic_bsd_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            str_0 = 'd'
            str_1 = 'azE['
            list_0 = []
            bytes_0 = b'c\x1a-tM\x191?\xc3\xa6\x9c\x15\x88\x91G\xfa\n'
            str_2 = ''
            str_3 = 'DAlikhIsQQ)7n8~sbR'
            dict_0 = {str_3: str_0, str_0: bytes_0}
            bytes_1 = b'E\x0c\xa1\xaa\xf8W\xf2'
            generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bytes_1)
            bytes_2 = b'\xb2'
            generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(bytes_2)
            var_0 = generic_bsd_ifconfig_network_1.parse_ether_line(bytes_0, dict_0, generic_bsd_ifconfig_network_0)
            dict_1 = {str_0: str_2}
            generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(bytes_0, dict_1)
            var_1 = generic_bsd_ifconfig_network_2.get_interfaces_info(str_1, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
