import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = True
            distribution_files_0 = module_0.DistributionFiles(bool_0)
            float_0 = 1.0
            tuple_0 = (float_0, bool_0)
            distribution_files_1 = module_0.DistributionFiles(tuple_0)
            dict_0 = {distribution_files_1: tuple_0}
            distribution_0 = module_0.Distribution(dict_0)
            float_1 = 2296.47603
            str_0 = 'B'
            str_1 = 'L=K'
            distribution_files_2 = module_0.DistributionFiles(str_1)
            distribution_files_3 = module_0.DistributionFiles(distribution_files_2)
            var_0 = distribution_files_3.parse_distribution_file_Slackware(distribution_files_0, distribution_0, float_1, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
