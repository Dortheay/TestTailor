import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = '(`$O/wWUD6my3In\x0b?'
        distribution_files_0 = module_0.DistributionFiles(str_0)
        var_0 = distribution_files_0.process_dist_files()
        set_0 = set()
        list_0 = [set_0, str_0, distribution_files_0, set_0]
        distribution_fact_collector_0 = module_0.DistributionFactCollector(distribution_files_0)
        bytes_0 = b'p7\x8cK\xb6U\x87\xdfT\x11\xb1\x01\xd2\xe4\xbd\x07r\x88'
        var_1 = distribution_files_0.parse_distribution_file_ClearLinux(str_0, list_0, distribution_fact_collector_0, bytes_0)

if __name__ == "__main__":
    unittest.main()
