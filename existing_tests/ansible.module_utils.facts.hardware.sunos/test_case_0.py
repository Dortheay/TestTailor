import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.sunos as module_0

class Test_Sunos_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        sun_o_s_hardware_collector_0 = module_0.SunOSHardwareCollector()

if __name__ == "__main__":
    unittest.main()
