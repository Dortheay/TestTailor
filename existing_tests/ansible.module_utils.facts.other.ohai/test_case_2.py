import unittest
import timeout_decorator
import ansible.module_utils.facts.other.ohai as module_0

class Test_Ohai_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '%s@%s %s %s'
            set_0 = {str_0}
            int_0 = 1446
            ohai_fact_collector_0 = module_0.OhaiFactCollector()
            var_0 = ohai_fact_collector_0.run_ohai(set_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
