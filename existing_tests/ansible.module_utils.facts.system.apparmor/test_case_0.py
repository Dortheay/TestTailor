import unittest
import timeout_decorator
import ansible.module_utils.facts.system.apparmor as module_0

class Test_Apparmor_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        apparmor_fact_collector_0 = module_0.ApparmorFactCollector()

if __name__ == "__main__":
    unittest.main()
