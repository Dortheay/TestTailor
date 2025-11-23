import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.hurd as module_0

class Test_Hurd_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        hurd_hardware_collector_0 = module_0.HurdHardwareCollector()

if __name__ == "__main__":
    unittest.main()
