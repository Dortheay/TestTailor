import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.darwin as module_0

class Test_Darwin_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            float_0 = -1164.5409
            darwin_hardware_0 = module_0.DarwinHardware(float_0, float_0)
            var_0 = darwin_hardware_0.get_cpu_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
