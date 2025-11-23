import unittest
import timeout_decorator
import ansible.module_utils.facts.network.darwin as module_0

class Test_Darwin_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bool_0 = False
        list_0 = [bool_0, bool_0]
        dict_0 = {}
        bytes_0 = b'\xa1\x06q#'
        bool_1 = False
        tuple_0 = (bytes_0, bool_1)
        darwin_network_collector_0 = module_0.DarwinNetworkCollector(bytes_0)
        darwin_network_collector_1 = module_0.DarwinNetworkCollector()
        dict_1 = {darwin_network_collector_0: darwin_network_collector_0, bytes_0: bytes_0}
        darwin_network_0 = module_0.DarwinNetwork(dict_1)
        var_0 = darwin_network_0.parse_media_line(list_0, dict_0, tuple_0)
        darwin_network_collector_2 = None
        set_0 = set()
        darwin_network_1 = module_0.DarwinNetwork(set_0)
        darwin_network_collector_3 = module_0.DarwinNetworkCollector(set_0)
        darwin_network_2 = module_0.DarwinNetwork(darwin_network_collector_2)

if __name__ == "__main__":
    unittest.main()
