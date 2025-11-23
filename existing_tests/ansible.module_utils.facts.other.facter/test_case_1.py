import unittest
import timeout_decorator
import ansible.module_utils.facts.other.facter as module_0

class Test_Facter_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            facter_fact_collector_0 = module_0.FacterFactCollector()
            str_0 = "k'6O*a\x0ck;W"
            var_0 = facter_fact_collector_0.get_facter_output(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
