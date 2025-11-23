import unittest
import timeout_decorator
import ansible.module_utils.facts.system.caps as module_0

class Test_Caps_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            system_capabilities_fact_collector_0 = module_0.SystemCapabilitiesFactCollector()
            var_0 = system_capabilities_fact_collector_0.collect()
            var_1 = system_capabilities_fact_collector_0.collect(system_capabilities_fact_collector_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
