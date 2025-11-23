import unittest
import timeout_decorator
import ansible.module_utils.facts.network.generic_bsd as module_0

class Test_Generic_bsd_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        list_0 = []
        str_0 = 'J|<oG/'
        bytes_0 = b'\x1d\x89~'
        str_1 = 'IByBbFKU;k(/F31~DHN'
        tuple_0 = (bytes_0, list_0, str_1, str_0)
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(tuple_0)
        var_0 = generic_bsd_ifconfig_network_0.get_options(str_0)

if __name__ == "__main__":
    unittest.main()
