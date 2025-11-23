import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.sunos as module_0

class Test_Sunos_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            set_0 = set()
            sun_o_s_hardware_0 = module_0.SunOSHardware(set_0)
            var_0 = sun_o_s_hardware_0.get_uptime_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
