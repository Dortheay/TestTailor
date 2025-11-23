import unittest
import timeout_decorator
import ansible.vars.fact_cache as module_0

class Test_Fact_cache_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '1fact1z'
            fact_cache_0 = module_0.FactCache()
            var_0 = fact_cache_0.first_order_merge(str_0, str_0)
            var_1 = fact_cache_0.first_order_merge(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
