import unittest
import timeout_decorator
import ansible.module_utils.facts.other.facter as module_0

class Test_Facter_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = 1032
            set_0 = {int_0, int_0}
            facter_fact_collector_0 = module_0.FacterFactCollector()
            var_0 = facter_fact_collector_0.run_facter(int_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
