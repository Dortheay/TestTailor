import unittest
import timeout_decorator
import ansible.module_utils.facts.system.distribution as module_0

class Test_Distribution_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            int_0 = None
            dict_0 = None
            str_0 = 'ubuntu'
            str_1 = "JTA$\nyX({+b'"
            tuple_0 = (int_0, dict_0, str_0, str_1)
            distribution_0 = module_0.Distribution(tuple_0)
            distribution_1 = module_0.Distribution(distribution_0)
            distribution_2 = module_0.Distribution(distribution_1)
            var_0 = distribution_2.get_distribution_NetBSD()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
