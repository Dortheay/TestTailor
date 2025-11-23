import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0
import collections as module_1

class Test_Collector_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            cycle_found_in_fact_deps_0 = None
            tuple_0 = None
            base_fact_collector_0 = module_0.BaseFactCollector(tuple_0)
            var_0 = module_0.collector_classes_from_gather_subset(cycle_found_in_fact_deps_0, base_fact_collector_0)
            var_1 = base_fact_collector_0.collect()
            unresolved_fact_dep_0 = module_0.UnresolvedFactDep()
            var_2 = base_fact_collector_0.collect_with_namespace()
            list_0 = []
            var_3 = module_0.resolve_requires(list_0, unresolved_fact_dep_0)
            collector_not_found_error_0 = module_0.CollectorNotFoundError()
            int_0 = 500
            int_1 = -203
            var_4 = module_0.find_collectors_for_platform(int_0, int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
