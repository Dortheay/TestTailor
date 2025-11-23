import unittest
import timeout_decorator
import ansible.module_utils.facts.network.hurd as module_0

class Test_Hurd_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        hurd_network_collector_0 = module_0.HurdNetworkCollector()

if __name__ == "__main__":
    unittest.main()
