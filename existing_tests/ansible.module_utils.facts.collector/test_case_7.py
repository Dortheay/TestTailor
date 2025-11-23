import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0
import collections as module_1

class Test_Collector_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            collector_not_found_error_0 = module_0.CollectorNotFoundError()
            bytes_0 = b'\x01@\xd5'
            float_0 = 693.7
            set_0 = None
            list_0 = []
            unresolved_fact_dep_0 = module_0.UnresolvedFactDep(*list_0)
            base_fact_collector_0 = module_0.BaseFactCollector(float_0, set_0)
            var_0 = module_0.resolve_requires(bytes_0, base_fact_collector_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
