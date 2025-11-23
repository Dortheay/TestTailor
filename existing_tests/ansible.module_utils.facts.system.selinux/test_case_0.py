import unittest
import timeout_decorator
import ansible.module_utils.facts.system.selinux as module_0

class Test_Selinux_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        selinux_fact_collector_0 = module_0.SelinuxFactCollector()

if __name__ == "__main__":
    unittest.main()
