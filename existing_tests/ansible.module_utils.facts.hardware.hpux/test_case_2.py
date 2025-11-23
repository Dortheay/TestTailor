import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.hpux as module_0

class Test_Hpux_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = "yf7`z[V}~D^'GWVKzq~\t"
            bytes_0 = b'\xbe\xb3'
            h_p_u_x_hardware_collector_0 = module_0.HPUXHardwareCollector(bytes_0)
            str_1 = 'sb1z~<NE?y#Xee)?eBCc'
            set_0 = {str_1, h_p_u_x_hardware_collector_0, str_1, str_1}
            h_p_u_x_hardware_0 = module_0.HPUXHardware(h_p_u_x_hardware_collector_0, set_0)
            int_0 = 148
            h_p_u_x_hardware_1 = module_0.HPUXHardware(h_p_u_x_hardware_0, int_0)
            var_0 = h_p_u_x_hardware_1.get_cpu_facts(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
