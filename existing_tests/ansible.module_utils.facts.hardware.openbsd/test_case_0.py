import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.openbsd as module_0

class Test_Openbsd_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        open_b_s_d_hardware_collector_0 = module_0.OpenBSDHardwareCollector()

if __name__ == "__main__":
    unittest.main()
