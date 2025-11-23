import unittest
import timeout_decorator
import ansible.module_utils.facts.network.aix as module_0

class Test_Aix_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = None
            list_0 = []
            a_i_x_network_0 = module_0.AIXNetwork(list_0)
            var_0 = a_i_x_network_0.get_interfaces_info(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
