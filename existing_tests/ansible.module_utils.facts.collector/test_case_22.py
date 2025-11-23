import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0

class Test_Collector_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        cycle_found_in_fact_deps_0 = module_0.CycleFoundInFactDeps()

if __name__ == "__main__":
    unittest.main()
