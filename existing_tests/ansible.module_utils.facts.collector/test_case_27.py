import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0

class Test_Collector_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = '\n    Join the original cmd based on manipulations by split_args().\n    This retains the original newlines and whitespaces.\n    '
        set_0 = {str_0, str_0}
        base_fact_collector_0 = module_0.BaseFactCollector()
        var_0 = base_fact_collector_0.collect_with_namespace()
        var_1 = module_0.get_collector_names(str_0, set_0, set_0)
        var_2 = module_0.get_collector_names()
        list_0 = []
        base_fact_collector_1 = module_0.BaseFactCollector()
        var_3 = base_fact_collector_1.collect_with_namespace()
        bytes_0 = b'\xc7\xf5\x11s+\xf3\xe5\xb9mZ\x17\xb7U'
        var_4 = module_0.collector_classes_from_gather_subset(list_0, bytes_0)
        unresolved_fact_dep_0 = module_0.UnresolvedFactDep()

if __name__ == "__main__":
    unittest.main()
