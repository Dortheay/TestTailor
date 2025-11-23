import unittest
import timeout_decorator
import ansible.module_utils.facts.network.hpux as module_0

class Test_Hpux_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '\x0bC& 3`8'
            int_0 = 768
            dict_0 = {int_0: int_0}
            h_p_u_x_network_0 = module_0.HPUXNetwork(int_0, dict_0)
            var_0 = h_p_u_x_network_0.populate(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
