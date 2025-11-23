import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.hpux as module_0

class Test_Hpux_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bool_0 = True
            h_p_u_x_hardware_0 = None
            list_0 = [h_p_u_x_hardware_0]
            list_1 = [list_0, list_0, h_p_u_x_hardware_0, h_p_u_x_hardware_0]
            int_0 = 3260
            bool_1 = False
            bytes_0 = b'\x07'
            h_p_u_x_hardware_collector_0 = module_0.HPUXHardwareCollector(bool_1, bytes_0)
            tuple_0 = (int_0, h_p_u_x_hardware_collector_0)
            tuple_1 = (list_1, tuple_0, int_0)
            h_p_u_x_hardware_1 = module_0.HPUXHardware(tuple_1)
            var_0 = h_p_u_x_hardware_1.get_hw_facts(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
