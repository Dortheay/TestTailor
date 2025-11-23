import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.freebsd as module_0

class Test_Freebsd_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            float_0 = 2307.345
            free_b_s_d_hardware_0 = module_0.FreeBSDHardware(float_0)
            var_0 = free_b_s_d_hardware_0.get_uptime_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
