import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = '#RSxC5\tb\x0cbj[\\_a'
            distribution_0 = module_0.Distribution(str_0)
            dict_0 = {str_0: distribution_0, str_0: str_0}
            list_0 = [dict_0]
            bool_0 = False
            distribution_files_0 = module_0.DistributionFiles(bool_0)
            var_0 = distribution_files_0.parse_distribution_file_OpenWrt(list_0, list_0, list_0, list_0)
            var_1 = distribution_0.get_distribution_HPUX()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
