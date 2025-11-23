import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.openbsd as module_0

class Test_Openbsd_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            list_0 = []
            open_b_s_d_hardware_0 = module_0.OpenBSDHardware(list_0)
            var_0 = open_b_s_d_hardware_0.populate()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
