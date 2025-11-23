import unittest
import timeout_decorator
import ansible.module_utils.facts.network.sunos as module_0

class Test_Sunos_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'ActiveState='
        sun_o_s_network_collector_0 = None
        set_0 = {str_0, str_0}
        float_0 = -252.0
        sun_o_s_network_0 = module_0.SunOSNetwork(float_0)
        var_0 = sun_o_s_network_0.parse_interface_line(str_0, sun_o_s_network_collector_0, set_0)

if __name__ == "__main__":
    unittest.main()
