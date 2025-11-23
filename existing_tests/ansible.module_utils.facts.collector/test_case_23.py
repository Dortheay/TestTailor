import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0

class Test_Collector_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        base_fact_collector_0 = module_0.BaseFactCollector()

if __name__ == "__main__":
    unittest.main()
