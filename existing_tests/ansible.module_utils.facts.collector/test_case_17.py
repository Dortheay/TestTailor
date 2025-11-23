import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0
import collections as module_1

class Test_Collector_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            str_0 = None
            list_0 = []
            dict_0 = {}
            bytes_0 = b'\xc6\xec3\xc6\x03\xcf\xe6\n2'
            var_0 = module_0.resolve_requires(bytes_0, bytes_0)
            list_1 = [list_0]
            base_fact_collector_0 = module_0.BaseFactCollector(list_1)
            var_1 = module_0.find_unresolved_requires(dict_0, base_fact_collector_0)
            bytes_1 = b'\xc7\xf5\x11s+\xf3\xe5\xb9mZ\x17\xb7U'
            collector_not_found_error_0 = module_0.CollectorNotFoundError()
            var_2 = module_0.collector_classes_from_gather_subset(list_0, bytes_1)
            unresolved_fact_dep_0 = module_0.UnresolvedFactDep()
            dict_1 = {}
            collector_not_found_error_1 = module_0.CollectorNotFoundError()
            list_2 = [dict_1, base_fact_collector_0, str_0]
            unresolved_fact_dep_1 = module_0.UnresolvedFactDep(*list_2)
            dict_2 = {}
            int_0 = 29
            var_3 = module_0.resolve_requires(dict_2, int_0)
            var_4 = base_fact_collector_0.collect_with_namespace()
            var_5 = module_0.get_collector_names(dict_1, int_0, base_fact_collector_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
