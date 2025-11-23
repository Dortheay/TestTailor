import unittest
import timeout_decorator
import ansible.module_utils.facts.other.ohai as module_0

class Test_Ohai_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            ohai_fact_collector_0 = module_0.OhaiFactCollector()
            var_0 = ohai_fact_collector_0.collect()
            bool_0 = True
            var_1 = ohai_fact_collector_0.collect(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
