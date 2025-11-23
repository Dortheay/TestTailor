import unittest
import timeout_decorator
import ansible.module_utils.facts.virtual.hpux as module_0

class Test_Hpux_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        float_0 = 256.48279
        h_p_u_x_virtual_0 = module_0.HPUXVirtual(float_0)
        var_0 = h_p_u_x_virtual_0.get_virtual_facts()

if __name__ == "__main__":
    unittest.main()
