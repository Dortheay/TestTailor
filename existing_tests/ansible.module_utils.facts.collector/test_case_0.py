import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0
import collections as module_1

class Test_Collector_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            unresolved_fact_dep_0 = module_0.UnresolvedFactDep()
            unresolved_fact_dep_1 = module_0.UnresolvedFactDep()
            list_0 = [unresolved_fact_dep_1, unresolved_fact_dep_0]
            defaultdict_0 = module_1.defaultdict()
            collector_not_found_error_0 = module_0.CollectorNotFoundError()
            base_fact_collector_0 = module_0.BaseFactCollector(defaultdict_0, collector_not_found_error_0)
            var_0 = base_fact_collector_0.collect(list_0)
            var_1 = base_fact_collector_0.collect_with_namespace()
            str_0 = 'min'
            var_2 = module_0.get_collector_names(str_0)
            unresolved_fact_dep_2 = module_0.UnresolvedFactDep()
            str_1 = '9;M%.'
            dict_0 = None
            var_3 = module_0.select_collector_classes(str_1, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
