import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.freebsd as module_0

class Test_Freebsd_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = -3665.0
            free_b_s_d_hardware_0 = module_0.FreeBSDHardware(float_0)
            var_0 = free_b_s_d_hardware_0.populate()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
