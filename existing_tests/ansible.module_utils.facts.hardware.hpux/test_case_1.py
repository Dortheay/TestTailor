import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.hpux as module_0

class Test_Hpux_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\xcf\xa0H\xf6B\xe5\xa0D\xa9f6\xcd\xe1(\xc1\x16'
            h_p_u_x_hardware_0 = module_0.HPUXHardware(bytes_0)
            h_p_u_x_hardware_1 = module_0.HPUXHardware(h_p_u_x_hardware_0)
            var_0 = h_p_u_x_hardware_1.get_hw_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
