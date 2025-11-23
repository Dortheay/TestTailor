import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            bytes_0 = b'r\xdd&\x17\x9bg'
            distribution_files_0 = module_0.DistributionFiles(bytes_0)
            distribution_fact_collector_0 = module_0.DistributionFactCollector()
            distribution_files_1 = module_0.DistributionFiles(distribution_fact_collector_0)
            tuple_0 = ()
            distribution_0 = module_0.Distribution(tuple_0)
            float_0 = 2970.7
            distribution_files_2 = module_0.DistributionFiles(float_0)
            var_0 = distribution_files_2.process_dist_files()
            var_1 = distribution_0.get_distribution_SunOS()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
