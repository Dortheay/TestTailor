import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        distribution_fact_collector_0 = module_0.DistributionFactCollector()
        distribution_0 = module_0.Distribution(distribution_fact_collector_0)

if __name__ == "__main__":
    unittest.main()
