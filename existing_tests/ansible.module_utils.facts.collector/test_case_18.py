import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0
import collections as module_1

class Test_Collector_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            str_0 = '\n    Join the original cmd based on manipulations by split_args().\n    This retains the original newlines and whitespaces.\n    '
            set_0 = {str_0, str_0, str_0, str_0}
            list_0 = [str_0, set_0, str_0]
            bytes_0 = b'\xaf\x87'
            base_fact_collector_0 = module_0.BaseFactCollector(list_0, bytes_0)
            var_0 = base_fact_collector_0.collect_with_namespace()
            str_1 = None
            list_1 = []
            dict_0 = {}
            list_2 = [list_1]
            base_fact_collector_1 = module_0.BaseFactCollector(list_2)
            var_1 = module_0.find_unresolved_requires(dict_0, base_fact_collector_1)
            bytes_1 = b'\xc7\xf5\x11s+\xf3\xe5\xb9mZ\x17\xb7U'
            var_2 = module_0.collector_classes_from_gather_subset(list_1, bytes_1)
            dict_1 = {}
            collector_not_found_error_0 = module_0.CollectorNotFoundError()
            list_3 = [dict_1, base_fact_collector_1, str_1]
            unresolved_fact_dep_0 = module_0.UnresolvedFactDep(*list_3)
            int_0 = 29
            var_3 = module_0.resolve_requires(dict_0, int_0)
            var_4 = base_fact_collector_1.collect_with_namespace()
            var_5 = module_0.get_collector_names(dict_1, int_0, unresolved_fact_dep_0, base_fact_collector_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
