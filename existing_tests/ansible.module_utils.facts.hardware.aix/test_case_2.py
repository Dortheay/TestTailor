import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.aix as module_0

class Test_Aix_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            tuple_0 = None
            set_0 = {tuple_0, tuple_0}
            a_i_x_hardware_0 = module_0.AIXHardware(set_0)
            var_0 = a_i_x_hardware_0.get_memory_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
