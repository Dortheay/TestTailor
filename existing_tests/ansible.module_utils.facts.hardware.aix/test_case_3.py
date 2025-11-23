import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.aix as module_0

class Test_Aix_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'E-.0 []6Q{a\n!'
            a_i_x_hardware_0 = module_0.AIXHardware(str_0)
            a_i_x_hardware_1 = module_0.AIXHardware(a_i_x_hardware_0)
            var_0 = a_i_x_hardware_1.get_dmi_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
