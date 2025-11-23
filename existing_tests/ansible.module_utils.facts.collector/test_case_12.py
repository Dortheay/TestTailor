import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0
import collections as module_1

class Test_Collector_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            base_fact_collector_0 = None
            dict_0 = {base_fact_collector_0: base_fact_collector_0}
            var_0 = module_0.tsort(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
