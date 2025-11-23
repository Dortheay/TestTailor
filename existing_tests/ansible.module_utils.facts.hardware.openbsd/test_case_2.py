import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.openbsd as module_0

class Test_Openbsd_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'Done in kid B.'
            bytes_0 = b'[\xef5\x99'
            dict_0 = {}
            open_b_s_d_hardware_0 = module_0.OpenBSDHardware(bytes_0, dict_0)
            open_b_s_d_hardware_1 = module_0.OpenBSDHardware(str_0, open_b_s_d_hardware_0)
            var_0 = open_b_s_d_hardware_1.get_memory_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
