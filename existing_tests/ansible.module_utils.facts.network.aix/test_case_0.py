import unittest
import timeout_decorator
import ansible.module_utils.facts.network.aix as module_0

class Test_Aix_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            a_i_x_network_collector_0 = module_0.AIXNetworkCollector()
            bool_0 = False
            bytes_0 = b'\xd8\x08b.-\xa5\x1c}='
            a_i_x_network_0 = module_0.AIXNetwork(bytes_0)
            var_0 = a_i_x_network_0.get_default_interfaces(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
