import unittest
import timeout_decorator
import ansible.module_utils.facts.network.generic_bsd as module_0

class Test_Generic_bsd_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            float_0 = -1472.87815
            set_0 = {float_0, float_0}
            bool_0 = False
            list_0 = [bool_0, bool_0, float_0, set_0]
            float_1 = -2754.665
            int_0 = None
            tuple_0 = (list_0,)
            generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
            var_0 = generic_bsd_ifconfig_network_0.parse_lladdr_line(float_1, int_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
