import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        float_0 = 2195.99
        distribution_files_0 = module_0.DistributionFiles(float_0)
        float_1 = 2599.0
        distribution_files_1 = module_0.DistributionFiles(float_1)
        str_0 = 'ubuntu'
        bytes_0 = None
        bool_0 = True
        var_0 = distribution_files_0.parse_distribution_file_Debian(str_0, str_0, bytes_0, bool_0)

if __name__ == "__main__":
    unittest.main()
