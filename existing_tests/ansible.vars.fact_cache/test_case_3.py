import unittest
import timeout_decorator
import ansible.vars.fact_cache as module_0

class Test_Fact_cache_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            dict_0 = None
            list_0 = [dict_0]
            fact_cache_0 = module_0.FactCache()
            var_0 = fact_cache_0.__contains__(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
