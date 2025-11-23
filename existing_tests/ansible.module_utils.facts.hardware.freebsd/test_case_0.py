import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.freebsd as module_0

class Test_Freebsd_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        free_b_s_d_hardware_collector_0 = module_0.FreeBSDHardwareCollector()

if __name__ == "__main__":
    unittest.main()
