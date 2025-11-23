import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            bytes_0 = None
            distribution_0 = module_0.Distribution(bytes_0)
            float_0 = None
            dict_0 = {float_0: float_0, float_0: float_0}
            distribution_1 = module_0.Distribution(dict_0)
            distribution_fact_collector_0 = module_0.DistributionFactCollector()
            var_0 = distribution_1.get_distribution_OpenBSD()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
