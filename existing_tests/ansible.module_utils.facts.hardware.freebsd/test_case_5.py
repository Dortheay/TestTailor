import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.freebsd as module_0

class Test_Freebsd_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = '4_X4('
            free_b_s_d_hardware_0 = module_0.FreeBSDHardware(str_0)
            var_0 = free_b_s_d_hardware_0.get_dmi_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
