import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'jwcn-s2'
            str_1 = '%s/%s/%s'
            distribution_0 = module_0.Distribution(str_1)
            dict_0 = {}
            distribution_fact_collector_0 = module_0.DistributionFactCollector()
            float_0 = -3864.56004
            distribution_files_0 = module_0.DistributionFiles(float_0)
            var_0 = distribution_files_0.parse_distribution_file_NA(str_0, distribution_0, dict_0, distribution_fact_collector_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
