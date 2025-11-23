import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.hpux as module_0

class Test_Hpux_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 1037
            h_p_u_x_hardware_0 = module_0.HPUXHardware(int_0)
            var_0 = h_p_u_x_hardware_0.populate()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
