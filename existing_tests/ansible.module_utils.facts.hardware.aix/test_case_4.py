import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.aix as module_0

class Test_Aix_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            set_0 = set()
            a_i_x_hardware_0 = module_0.AIXHardware(set_0)
            var_0 = a_i_x_hardware_0.get_vgs_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
