import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        float_0 = 0.5
        str_0 = "oCL'2="
        str_1 = ' ""GdN1(a'
        list_0 = [str_1, str_1, str_1]
        distribution_files_0 = module_0.DistributionFiles(list_0)
        float_1 = 60.0
        distribution_files_1 = module_0.DistributionFiles(float_1)
        var_0 = distribution_files_1.parse_distribution_file_Mandriva(float_0, str_0, str_0, str_1)

if __name__ == "__main__":
    unittest.main()
