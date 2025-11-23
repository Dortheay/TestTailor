import unittest
import timeout_decorator
import ansible.module_utils.facts.other.facter as module_0

class Test_Facter_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            facter_fact_collector_0 = module_0.FacterFactCollector()
            var_0 = facter_fact_collector_0.collect()
            var_1 = facter_fact_collector_0.collect(facter_fact_collector_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
