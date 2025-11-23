import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        distribution_fact_collector_0 = module_0.DistributionFactCollector()
        int_0 = 2825
        str_0 = '\x0bV]~aLK}t'
        set_0 = {int_0, distribution_fact_collector_0}
        tuple_0 = (int_0, str_0, set_0)
        distribution_files_0 = module_0.DistributionFiles(tuple_0)
        dict_0 = {int_0: tuple_0}
        str_1 = 'w%\x0cABnC[G[ a^SI!'
        distribution_files_1 = module_0.DistributionFiles(str_1)
        var_0 = distribution_files_1.parse_distribution_file_Flatcar(distribution_fact_collector_0, distribution_files_0, dict_0, distribution_fact_collector_0)

if __name__ == "__main__":
    unittest.main()
