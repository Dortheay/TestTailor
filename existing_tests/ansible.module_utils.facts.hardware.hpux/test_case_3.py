import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.hpux as module_0

class Test_Hpux_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            float_0 = 0.2
            bytes_0 = b'\xa8\xc8\x90y'
            h_p_u_x_hardware_0 = module_0.HPUXHardware(bytes_0)
            var_0 = h_p_u_x_hardware_0.get_memory_facts(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
