import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0
import collections as module_1

class Test_Collector_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        try:
            dict_0 = None
            base_fact_collector_0 = module_0.BaseFactCollector(dict_0)
            list_0 = [base_fact_collector_0, dict_0, dict_0]
            base_fact_collector_1 = module_0.BaseFactCollector()
            var_0 = module_0.build_fact_id_to_collector_map(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
