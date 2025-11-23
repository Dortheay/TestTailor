import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        distribution_fact_collector_0 = module_0.DistributionFactCollector()
        distribution_0 = module_0.Distribution(distribution_fact_collector_0)
        var_0 = distribution_0.get_distribution_FreeBSD()

if __name__ == "__main__":
    unittest.main()
