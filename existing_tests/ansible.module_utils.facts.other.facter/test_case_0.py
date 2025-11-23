import unittest
import timeout_decorator
import ansible.module_utils.facts.other.facter as module_0

class Test_Facter_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        facter_fact_collector_0 = module_0.FacterFactCollector()

if __name__ == "__main__":
    unittest.main()
