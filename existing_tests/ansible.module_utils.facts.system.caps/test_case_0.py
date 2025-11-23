import unittest
import timeout_decorator
import ansible.module_utils.facts.system.caps as module_0

class Test_Caps_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        system_capabilities_fact_collector_0 = module_0.SystemCapabilitiesFactCollector()

if __name__ == "__main__":
    unittest.main()
