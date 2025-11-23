import unittest
import timeout_decorator
import ansible.module_utils.facts.system.local as module_0

class Test_Local_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        local_fact_collector_0 = module_0.LocalFactCollector()

if __name__ == "__main__":
    unittest.main()
