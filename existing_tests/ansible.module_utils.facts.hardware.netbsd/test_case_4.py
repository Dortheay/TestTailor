import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.netbsd as module_0

class Test_Netbsd_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bool_0 = True
        net_b_s_d_hardware_0 = module_0.NetBSDHardware(bool_0)
        var_0 = net_b_s_d_hardware_0.get_memory_facts()

if __name__ == "__main__":
    unittest.main()
