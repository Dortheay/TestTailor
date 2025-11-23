import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        float_0 = 1988.927
        dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
        bool_0 = False
        str_0 = 'rescued'
        distribution_files_0 = module_0.DistributionFiles(str_0)
        var_0 = distribution_files_0.parse_distribution_file_Coreos(float_0, dict_0, bool_0, distribution_files_0)

if __name__ == "__main__":
    unittest.main()
