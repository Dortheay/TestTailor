import unittest
import timeout_decorator
import ansible.module_utils.facts.system.local as module_0

class Test_Local_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            local_fact_collector_0 = module_0.LocalFactCollector()
            var_0 = local_fact_collector_0.collect(local_fact_collector_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
