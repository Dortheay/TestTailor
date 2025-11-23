import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = "AKLlf#>^JnOtk$'\n}"
            distribution_fact_collector_0 = module_0.DistributionFactCollector(str_0)
            var_0 = distribution_fact_collector_0.collect()
            distribution_0 = module_0.Distribution(distribution_fact_collector_0)
            var_1 = distribution_0.get_distribution_DragonFly()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
