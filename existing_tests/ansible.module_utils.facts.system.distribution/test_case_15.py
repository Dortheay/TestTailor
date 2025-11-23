import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = -1809.927
            set_0 = {float_0}
            distribution_fact_collector_0 = module_0.DistributionFactCollector(set_0)
            distribution_0 = None
            distribution_1 = module_0.Distribution(distribution_0)
            distribution_files_0 = module_0.DistributionFiles(set_0)
            var_0 = module_0.get_uname(distribution_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
