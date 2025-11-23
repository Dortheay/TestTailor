import unittest
import timeout_decorator
import ansible.vars.fact_cache as module_0

class Test_Fact_cache_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        fact_cache_0 = module_0.FactCache()
        bytes_0 = b'\x8e\xab\xd4\x83?'
        int_0 = 1568
        var_0 = fact_cache_0.first_order_merge(bytes_0, int_0)
        var_1 = fact_cache_0.flush()

if __name__ == "__main__":
    unittest.main()
