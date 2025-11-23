import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0
import collections as module_1

class Test_Collector_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = 'y'
            dict_0 = {str_0: str_0, str_0: str_0}
            set_0 = set()
            tuple_0 = (dict_0, dict_0, set_0)
            unresolved_fact_dep_0 = None
            list_0 = None
            list_1 = [list_0, set_0, unresolved_fact_dep_0, unresolved_fact_dep_0]
            var_0 = module_0.collector_classes_from_gather_subset(tuple_0, unresolved_fact_dep_0, list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
