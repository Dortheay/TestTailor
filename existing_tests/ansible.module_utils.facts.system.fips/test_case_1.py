import unittest
import timeout_decorator
import ansible.module_utils.facts.system.fips as module_0

class Test_Fips_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        fips_fact_collector_0 = module_0.FipsFactCollector()
        var_0 = fips_fact_collector_0.collect()

if __name__ == "__main__":
    unittest.main()
