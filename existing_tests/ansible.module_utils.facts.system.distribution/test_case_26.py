import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            distribution_fact_collector_0 = None
            distribution_fact_collector_1 = module_0.DistributionFactCollector(distribution_fact_collector_0)
            float_0 = -992.180404
            bytes_0 = b'\xb5\xda\xc9b\xf3\xff\xdaEL\x9d\xcb\xce2'
            int_0 = 1608
            distribution_0 = module_0.Distribution(int_0)
            bytes_1 = b'z\xdc\xc0\xab\xf9\xec\xdb\x9c^\xcag?\x86\x19\xce1\xb0\xd3\xac\x9c'
            distribution_files_0 = module_0.DistributionFiles(bytes_1)
            distribution_1 = module_0.Distribution(distribution_files_0)
            var_0 = distribution_1.get_distribution_facts()
            list_0 = [bytes_0, float_0]
            distribution_files_1 = module_0.DistributionFiles(list_0)
            str_0 = '::N\x0b$[%T38+"f\x0cX*'
            tuple_0 = (str_0,)
            var_1 = module_0.get_uname(tuple_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
