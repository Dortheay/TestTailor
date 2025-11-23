import unittest
import timeout_decorator
import ansible.module_utils.facts.network.linux as module_0

class Test_Linux_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        linux_network_collector_0 = module_0.LinuxNetworkCollector()

if __name__ == "__main__":
    unittest.main()
