import unittest
import timeout_decorator
import ansible.module_utils.facts.network.hpux as module_0

class Test_Hpux_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = -282.759138
            h_p_u_x_network_0 = module_0.HPUXNetwork(float_0)
            var_0 = h_p_u_x_network_0.get_default_interfaces()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
