import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.darwin as module_0

class Test_Darwin_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        darwin_hardware_collector_0 = module_0.DarwinHardwareCollector()

if __name__ == "__main__":
    unittest.main()
