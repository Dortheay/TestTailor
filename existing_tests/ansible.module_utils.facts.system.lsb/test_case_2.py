import unittest
import timeout_decorator
import ansible.module_utils.facts.system.lsb as module_0

class Test_Lsb_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        l_s_b_fact_collector_0 = module_0.LSBFactCollector()
        var_0 = l_s_b_fact_collector_0.collect()

if __name__ == "__main__":
    unittest.main()
