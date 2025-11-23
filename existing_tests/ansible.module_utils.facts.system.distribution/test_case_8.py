import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        bool_0 = True
        set_0 = {bool_0, bool_0, bool_0}
        list_0 = [set_0]
        str_0 = 'VxM;0"VKl\x0b5TW;9k=-wE'
        distribution_files_0 = module_0.DistributionFiles(str_0)
        float_0 = 0.2
        distribution_files_1 = module_0.DistributionFiles(float_0)
        var_0 = distribution_files_1.parse_distribution_file_CentOS(set_0, list_0, distribution_files_0, distribution_files_0)

if __name__ == "__main__":
    unittest.main()
