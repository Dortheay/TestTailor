import unittest
import timeout_decorator
import ansible.vars.fact_cache as module_0

class Test_Fact_cache_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        fact_cache_0 = module_0.FactCache()

if __name__ == "__main__":
    unittest.main()
