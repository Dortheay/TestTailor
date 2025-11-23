import unittest
import timeout_decorator
import ansible.module_utils.facts.network.darwin as module_0

class Test_Darwin_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        dict_0 = {}
        darwin_network_collector_0 = module_0.DarwinNetworkCollector()
        darwin_network_0 = module_0.DarwinNetwork(darwin_network_collector_0)
        darwin_network_collector_1 = module_0.DarwinNetworkCollector()
        set_0 = set()
        darwin_network_1 = module_0.DarwinNetwork(darwin_network_0)
        str_0 = '<uknown'
        var_0 = darwin_network_0.parse_media_line(str_0, dict_0, set_0)

if __name__ == "__main__":
    unittest.main()
