import unittest
import timeout_decorator
import ansible.module_utils.facts.system.caps as module_0

class Test_Caps_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        system_capabilities_fact_collector_0 = module_0.SystemCapabilitiesFactCollector()
        var_0 = system_capabilities_fact_collector_0.collect()

if __name__ == "__main__":
    unittest.main()
