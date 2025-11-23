import unittest
import timeout_decorator
import ansible.module_utils.facts.network.aix as module_0

class Test_Aix_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            set_0 = set()
            int_0 = 1850
            a_i_x_network_0 = module_0.AIXNetwork(int_0)
            var_0 = a_i_x_network_0.parse_interface_line(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
