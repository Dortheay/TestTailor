import unittest
import timeout_decorator
import ansible.module_utils.facts.network.linux as module_0

class Test_Linux_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            int_0 = 1555
            float_0 = 0.1
            str_0 = 'zPT!ji'
            linux_network_0 = module_0.LinuxNetwork(float_0, str_0)
            var_0 = linux_network_0.get_ethtool_data(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
