import unittest
import timeout_decorator
import ansible.module_utils.facts.system.lsb as module_0

class Test_Lsb_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        l_s_b_fact_collector_0 = module_0.LSBFactCollector()

if __name__ == "__main__":
    unittest.main()
