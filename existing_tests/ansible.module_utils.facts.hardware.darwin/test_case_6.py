import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.darwin as module_0

class Test_Darwin_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            darwin_hardware_collector_0 = module_0.DarwinHardwareCollector()
            darwin_hardware_0 = module_0.DarwinHardware(darwin_hardware_collector_0)
            var_0 = darwin_hardware_0.get_uptime_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
