import unittest
import timeout_decorator
import ansible.module_utils.facts.network.linux as module_0

class Test_Linux_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bool_0 = None
            set_0 = {bool_0, bool_0, bool_0}
            str_0 = 'v>'
            linux_network_collector_0 = module_0.LinuxNetworkCollector()
            linux_network_collector_1 = module_0.LinuxNetworkCollector(str_0, linux_network_collector_0)
            linux_network_0 = module_0.LinuxNetwork(linux_network_collector_1)
            var_0 = linux_network_0.get_default_interfaces(bool_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
