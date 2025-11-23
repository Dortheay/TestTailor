import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0
import collections as module_1

class Test_Collector_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            dict_0 = {}
            cycle_found_in_fact_deps_0 = module_0.CycleFoundInFactDeps(**dict_0)
            str_0 = 't69E})f+GB'
            var_0 = module_0.resolve_requires(cycle_found_in_fact_deps_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
