import unittest
import timeout_decorator
import ansible.module_utils.facts.virtual.freebsd as module_0

class Test_Freebsd_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        free_b_s_d_virtual_collector_0 = module_0.FreeBSDVirtualCollector()

if __name__ == "__main__":
    unittest.main()
