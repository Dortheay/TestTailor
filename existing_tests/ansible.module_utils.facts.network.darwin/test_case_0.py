import unittest
import timeout_decorator
import ansible.module_utils.facts.network.darwin as module_0

class Test_Darwin_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = -129.733
            str_0 = 'P5Rf0\x0cM9yKO2o /s-b'
            int_0 = 1930
            darwin_network_collector_0 = module_0.DarwinNetworkCollector(int_0, float_0)
            set_0 = set()
            darwin_network_0 = module_0.DarwinNetwork(set_0)
            var_0 = darwin_network_0.parse_media_line(float_0, str_0, darwin_network_collector_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
