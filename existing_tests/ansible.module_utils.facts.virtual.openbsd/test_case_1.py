import unittest
import timeout_decorator
import ansible.module_utils.facts.virtual.openbsd as module_0

class Test_Openbsd_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        open_b_s_d_virtual_collector_0 = module_0.OpenBSDVirtualCollector()

if __name__ == "__main__":
    unittest.main()
