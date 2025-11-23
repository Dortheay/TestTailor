import unittest
import timeout_decorator
import ansible.module_utils.facts.network.aix as module_0

class Test_Aix_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        a_i_x_network_collector_0 = module_0.AIXNetworkCollector()

if __name__ == "__main__":
    unittest.main()
