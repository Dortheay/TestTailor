import unittest
import timeout_decorator
import ansible.module_utils.facts.network.linux as module_0

class Test_Linux_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'r\r1aDH\n\nGT%Zf1PJi:L'
            linux_network_0 = module_0.LinuxNetwork(str_0)
            linux_network_1 = module_0.LinuxNetwork(linux_network_0)
            linux_network_2 = module_0.LinuxNetwork(linux_network_1)
            var_0 = linux_network_2.populate()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
