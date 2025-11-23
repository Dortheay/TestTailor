import unittest
import timeout_decorator
import ansible.module_utils.facts.virtual.netbsd as module_0

class Test_Netbsd_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        net_b_s_d_virtual_collector_0 = module_0.NetBSDVirtualCollector()

if __name__ == "__main__":
    unittest.main()
