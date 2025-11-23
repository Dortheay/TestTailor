import unittest
import timeout_decorator
import ansible.module_utils.facts.network.generic_bsd as module_0

class Test_Generic_bsd_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bool_0 = True
            int_0 = -893
            int_1 = -1509
            generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_1)
            var_0 = generic_bsd_ifconfig_network_0.parse_unknown_line(bool_0, int_0, bool_0)
            str_0 = 'tq`cuU='
            dict_0 = {int_0: str_0}
            bytes_0 = b'\xde\xd7N\xaa\xa31\x17\x9aF>t\x8d_9'
            var_1 = generic_bsd_ifconfig_network_0.parse_nd6_line(dict_0, bytes_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
