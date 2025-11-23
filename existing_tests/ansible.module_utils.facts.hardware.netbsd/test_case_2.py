import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.netbsd as module_0

class Test_Netbsd_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        net_b_s_d_hardware_collector_0 = module_0.NetBSDHardwareCollector()

if __name__ == "__main__":
    unittest.main()
