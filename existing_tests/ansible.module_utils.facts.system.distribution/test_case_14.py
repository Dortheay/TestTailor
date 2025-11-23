import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        bytes_0 = b'\xb3S\x99\xbd\xd9\xc6\x01\xcda'
        distribution_0 = module_0.Distribution(bytes_0)
        var_0 = distribution_0.get_distribution_SMGL()
        dict_0 = {distribution_0: var_0}
        str_0 = 'n!w<rNn?'
        set_0 = {bytes_0}
        float_0 = 364.3
        set_1 = set()
        distribution_files_0 = module_0.DistributionFiles(set_1)
        var_1 = distribution_files_0.parse_distribution_file_NA(dict_0, str_0, set_0, float_0)
        bytes_1 = b'\x85\x9fL\x8f9?j/\x8an'
        distribution_fact_collector_0 = module_0.DistributionFactCollector(bytes_1)
        var_2 = distribution_files_0.parse_distribution_file_Flatcar(distribution_0, float_0, distribution_0, set_1)
        var_3 = distribution_0.get_distribution_FreeBSD()

if __name__ == "__main__":
    unittest.main()
