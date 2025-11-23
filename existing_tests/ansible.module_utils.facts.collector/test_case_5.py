import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0
import collections as module_1

class Test_Collector_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'python_target.py'
            dict_0 = {}
            cycle_found_in_fact_deps_0 = module_0.CycleFoundInFactDeps()
            var_0 = module_0.find_unresolved_requires(str_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
