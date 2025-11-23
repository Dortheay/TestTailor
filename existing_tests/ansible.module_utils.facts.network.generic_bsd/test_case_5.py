import unittest
import timeout_decorator
import ansible.module_utils.facts.network.generic_bsd as module_0

class Test_Generic_bsd_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = 1891
            bytes_0 = b'3{<|\xe4\xe2\xbd\xf9H'
            dict_0 = {bytes_0: bytes_0}
            bytes_1 = b'\xe8+at\xd0\xdc\xc5\x1e\x86\x0c-\x00\x84A-\xb8\x8a'
            generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(dict_0, bytes_1)
            var_0 = generic_bsd_ifconfig_network_0.get_interfaces_info(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
