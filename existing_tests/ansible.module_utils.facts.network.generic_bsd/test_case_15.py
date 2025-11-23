import unittest
import timeout_decorator
import ansible.module_utils.facts.network.generic_bsd as module_0

class Test_Generic_bsd_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            str_0 = '7gk]HPnU'
            int_0 = -1820
            generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0)
            var_0 = generic_bsd_ifconfig_network_0.populate(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
