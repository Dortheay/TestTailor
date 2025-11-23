import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            set_0 = set()
            bytes_0 = b'\x89\x1cY'
            str_0 = 'vQ=CFS:SLkei,^~v'
            distribution_0 = module_0.Distribution(str_0)
            list_0 = [set_0, bytes_0, set_0, distribution_0]
            distribution_files_0 = module_0.DistributionFiles(list_0)
            list_1 = [bytes_0]
            distribution_1 = module_0.Distribution(list_1)
            var_0 = distribution_1.get_distribution_FreeBSD()
            str_1 = 'Vault should be in the form of a string, instead we got: %s'
            distribution_fact_collector_0 = module_0.DistributionFactCollector()
            var_1 = distribution_fact_collector_0.collect(bytes_0, str_1)
            distribution_2 = module_0.Distribution(set_0)
            var_2 = distribution_2.get_distribution_AIX()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
