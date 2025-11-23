import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.aix as module_0

class Test_Aix_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        a_i_x_hardware_collector_0 = module_0.AIXHardwareCollector()

if __name__ == "__main__":
    unittest.main()
