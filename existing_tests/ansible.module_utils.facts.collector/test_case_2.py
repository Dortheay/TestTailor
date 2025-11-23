import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0
import collections as module_1

class Test_Collector_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = True
            set_0 = {bool_0}
            var_0 = module_0.build_fact_id_to_collector_map(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
