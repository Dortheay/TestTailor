import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.sunos as module_0

class Test_Sunos_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            set_0 = set()
            sun_o_s_hardware_0 = module_0.SunOSHardware(set_0)
            var_0 = sun_o_s_hardware_0.populate()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
