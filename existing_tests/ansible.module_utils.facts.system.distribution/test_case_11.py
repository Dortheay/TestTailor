import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        int_0 = 1280
        tuple_0 = (int_0,)
        distribution_fact_collector_0 = module_0.DistributionFactCollector()
        var_0 = distribution_fact_collector_0.collect(tuple_0)

if __name__ == "__main__":
    unittest.main()
