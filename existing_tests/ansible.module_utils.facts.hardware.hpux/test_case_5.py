import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.hpux as module_0

class Test_Hpux_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        h_p_u_x_hardware_collector_0 = module_0.HPUXHardwareCollector()

if __name__ == "__main__":
    unittest.main()
