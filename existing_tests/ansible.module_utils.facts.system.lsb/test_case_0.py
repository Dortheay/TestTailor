import unittest
import timeout_decorator
import ansible.module_utils.facts.system.lsb as module_0

class Test_Lsb_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            l_s_b_fact_collector_0 = module_0.LSBFactCollector()
            var_0 = l_s_b_fact_collector_0.collect()
            list_0 = [l_s_b_fact_collector_0]
            var_1 = l_s_b_fact_collector_0.collect(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
