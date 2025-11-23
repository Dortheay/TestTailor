import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.openbsd as module_0

class Test_Openbsd_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            open_b_s_d_hardware_collector_0 = module_0.OpenBSDHardwareCollector()
            open_b_s_d_hardware_0 = module_0.OpenBSDHardware(open_b_s_d_hardware_collector_0)
            dict_0 = {open_b_s_d_hardware_0: open_b_s_d_hardware_collector_0}
            open_b_s_d_hardware_1 = module_0.OpenBSDHardware(dict_0)
            var_0 = open_b_s_d_hardware_1.get_device_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
