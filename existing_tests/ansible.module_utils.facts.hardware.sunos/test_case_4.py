import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.sunos as module_0

class Test_Sunos_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bool_0 = False
            dict_0 = {bool_0: bool_0}
            sun_o_s_hardware_0 = module_0.SunOSHardware(dict_0)
            var_0 = sun_o_s_hardware_0.get_dmi_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
