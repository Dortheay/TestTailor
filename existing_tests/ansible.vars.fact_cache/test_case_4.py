import unittest
import timeout_decorator
import ansible.vars.fact_cache as module_0

class Test_Fact_cache_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = "998j A'w NuHpY"
            list_0 = None
            fact_cache_0 = module_0.FactCache()
            var_0 = fact_cache_0.first_order_merge(list_0, fact_cache_0)
            var_1 = fact_cache_0.__len__()
            var_2 = fact_cache_0.__iter__()
            var_3 = fact_cache_0.__getitem__(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
