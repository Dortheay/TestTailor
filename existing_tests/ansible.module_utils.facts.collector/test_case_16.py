import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0
import collections as module_1

class Test_Collector_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            bytes_0 = b'\xdc\x89o\x1f\x04`\x8a\x9d@N\xda\x06\x9de'
            dict_0 = {}
            var_0 = module_0.select_collector_classes(bytes_0, dict_0)
            cycle_found_in_fact_deps_0 = module_0.CycleFoundInFactDeps()
            collector_not_found_error_0 = module_0.CollectorNotFoundError()
            int_0 = 500
            int_1 = -203
            var_1 = module_0.find_collectors_for_platform(int_0, int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
