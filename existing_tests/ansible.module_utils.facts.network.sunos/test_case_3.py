import unittest
import timeout_decorator
import ansible.module_utils.facts.network.sunos as module_0

class Test_Sunos_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'WGgd(u5D?KCX vGx'
            sun_o_s_network_0 = module_0.SunOSNetwork(str_0)
            sun_o_s_network_collector_0 = module_0.SunOSNetworkCollector(sun_o_s_network_0)
            float_0 = 0.1
            sun_o_s_network_1 = module_0.SunOSNetwork(float_0)
            str_1 = 'P cy)bG.J'
            bool_0 = False
            sun_o_s_network_2 = module_0.SunOSNetwork(bool_0)
            str_2 = 'U"e G{9I{3{m'
            var_0 = sun_o_s_network_1.parse_interface_line(str_1, sun_o_s_network_2, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
