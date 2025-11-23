import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.aix as module_0

class Test_Aix_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            float_0 = 396.425185
            str_0 = 'n'
            bool_0 = None
            a_i_x_hardware_0 = module_0.AIXHardware(bool_0)
            float_1 = 0.1
            bool_1 = False
            a_i_x_hardware_collector_0 = module_0.AIXHardwareCollector(bool_1)
            dict_0 = {float_0: str_0, float_1: str_0, str_0: a_i_x_hardware_collector_0, str_0: a_i_x_hardware_collector_0}
            a_i_x_hardware_1 = module_0.AIXHardware(dict_0)
            var_0 = a_i_x_hardware_1.get_device_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
