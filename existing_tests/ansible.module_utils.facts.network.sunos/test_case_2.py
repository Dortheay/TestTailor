import unittest
import timeout_decorator
import ansible.module_utils.facts.network.sunos as module_0

class Test_Sunos_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            sun_o_s_network_collector_0 = module_0.SunOSNetworkCollector()
            bool_0 = True
            sun_o_s_network_0 = module_0.SunOSNetwork(bool_0)
            str_0 = '"bC'
            bytes_0 = b'\xeb\x18'
            var_0 = sun_o_s_network_0.parse_ether_line(str_0, sun_o_s_network_collector_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
