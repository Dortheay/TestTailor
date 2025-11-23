import unittest
import timeout_decorator
import ansible.vars.fact_cache as module_0

class Test_Fact_cache_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            fact_cache_0 = module_0.FactCache()
            bytes_0 = b'S@'
            int_0 = 1568
            var_0 = fact_cache_0.first_order_merge(bytes_0, int_0)
            str_0 = '--become'
            var_1 = fact_cache_0.__delitem__(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
