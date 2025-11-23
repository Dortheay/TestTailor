import unittest
import timeout_decorator
import ansible.module_utils.facts.network.linux as module_0

class Test_Linux_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'za\n'
            bool_0 = False
            linux_network_0 = module_0.LinuxNetwork(bool_0)
            var_0 = linux_network_0.get_default_interfaces(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
