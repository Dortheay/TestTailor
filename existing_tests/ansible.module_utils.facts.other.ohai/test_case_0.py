import unittest
import timeout_decorator
import ansible.module_utils.facts.other.ohai as module_0

class Test_Ohai_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        ohai_fact_collector_0 = module_0.OhaiFactCollector()

if __name__ == "__main__":
    unittest.main()
