import unittest
import timeout_decorator
import ansible.module_utils.facts.network.darwin as module_0

class Test_Darwin_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        darwin_network_collector_0 = module_0.DarwinNetworkCollector()

if __name__ == "__main__":
    unittest.main()
