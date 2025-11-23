import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.aix as module_0

class Test_Aix_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            a_i_x_hardware_collector_0 = module_0.AIXHardwareCollector()
            str_0 = 'Unable to retrieve file contents'
            a_i_x_hardware_0 = module_0.AIXHardware(a_i_x_hardware_collector_0, str_0)
            var_0 = a_i_x_hardware_0.get_mount_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
