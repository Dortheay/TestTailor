import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.openbsd as module_0

class Test_Openbsd_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bool_0 = True
            list_0 = [bool_0]
            open_b_s_d_hardware_collector_0 = module_0.OpenBSDHardwareCollector(list_0)
            list_1 = [open_b_s_d_hardware_collector_0]
            open_b_s_d_hardware_0 = module_0.OpenBSDHardware(list_1)
            var_0 = open_b_s_d_hardware_0.get_processor_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
