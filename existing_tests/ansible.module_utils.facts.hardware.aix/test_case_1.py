import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.aix as module_0

class Test_Aix_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = 0.0001
            set_0 = set()
            a_i_x_hardware_0 = module_0.AIXHardware(float_0, set_0)
            var_0 = a_i_x_hardware_0.populate()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
