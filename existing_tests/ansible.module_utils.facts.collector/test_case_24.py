import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0

class Test_Collector_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        cycle_found_in_fact_deps_0 = module_0.CycleFoundInFactDeps()
        base_fact_collector_0 = module_0.BaseFactCollector()
        var_0 = base_fact_collector_0.collect_with_namespace(cycle_found_in_fact_deps_0)

if __name__ == "__main__":
    unittest.main()
