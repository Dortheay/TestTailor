import unittest
import timeout_decorator
import ansible.module_utils.facts.system.fips as module_0

class Test_Fips_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        fips_fact_collector_0 = module_0.FipsFactCollector()

if __name__ == "__main__":
    unittest.main()
