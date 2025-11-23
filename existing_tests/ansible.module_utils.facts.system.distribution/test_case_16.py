import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '.%'
            distribution_files_0 = module_0.DistributionFiles(str_0)
            list_0 = [distribution_files_0]
            int_0 = -2240
            distribution_fact_collector_0 = module_0.DistributionFactCollector()
            str_1 = '^"'
            tuple_0 = (distribution_files_0,)
            distribution_fact_collector_1 = module_0.DistributionFactCollector()
            distribution_0 = module_0.Distribution(tuple_0)
            set_0 = {int_0, distribution_0, int_0}
            var_0 = distribution_files_0.parse_distribution_file_Coreos(str_1, distribution_0, set_0, list_0)
            float_0 = 1442.8496
            str_2 = 'TmN\r05\x0ba\nL}0\r'
            dict_0 = None
            var_1 = distribution_files_0.parse_distribution_file_Slackware(float_0, str_2, distribution_files_0, dict_0)
            str_3 = ',O'
            float_1 = -567.099771
            bytes_0 = b'\xec\x87\xd6k\xd1\xd1x\xd5G\x84A\x1f\xa5P'
            int_1 = -1501
            var_2 = distribution_files_0.parse_distribution_file_SUSE(str_3, float_1, bytes_0, int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
