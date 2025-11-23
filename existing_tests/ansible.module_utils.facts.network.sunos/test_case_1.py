import unittest
import timeout_decorator
import ansible.module_utils.facts.network.sunos as module_0

class Test_Sunos_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'erlang'
            sun_o_s_network_collector_0 = module_0.SunOSNetworkCollector(str_0)
            sun_o_s_network_0 = module_0.SunOSNetwork(str_0)
            set_0 = {str_0, sun_o_s_network_0}
            bool_0 = False
            sun_o_s_network_1 = module_0.SunOSNetwork(bool_0)
            var_0 = sun_o_s_network_1.parse_ether_line(sun_o_s_network_0, set_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
