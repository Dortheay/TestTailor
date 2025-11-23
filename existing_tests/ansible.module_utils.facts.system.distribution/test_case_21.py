import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            distribution_fact_collector_0 = module_0.DistributionFactCollector()
            distribution_0 = module_0.Distribution(distribution_fact_collector_0)
            distribution_1 = module_0.Distribution(distribution_0)
            distribution_2 = module_0.Distribution(distribution_1)
            var_0 = distribution_2.get_distribution_Darwin()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
