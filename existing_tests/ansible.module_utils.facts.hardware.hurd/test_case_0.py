import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.hurd as module_0

class Test_Hurd_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            hurd_hardware_collector_0 = module_0.HurdHardwareCollector()
            hurd_hardware_0 = module_0.HurdHardware(hurd_hardware_collector_0, hurd_hardware_collector_0)
            var_0 = hurd_hardware_0.populate()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
