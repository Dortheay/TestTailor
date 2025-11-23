import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.openbsd as module_0

class Test_Openbsd_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = "e\nL&mh'b"
            open_b_s_d_hardware_0 = module_0.OpenBSDHardware(str_0)
            var_0 = open_b_s_d_hardware_0.get_uptime_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
