import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.freebsd as module_0

class Test_Freebsd_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        int_0 = -2667
        free_b_s_d_hardware_0 = module_0.FreeBSDHardware(int_0)
        var_0 = free_b_s_d_hardware_0.get_device_facts()

if __name__ == "__main__":
    unittest.main()
