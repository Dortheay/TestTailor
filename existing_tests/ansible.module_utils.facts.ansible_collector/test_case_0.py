import unittest
import timeout_decorator
import ansible.module_utils.facts.ansible_collector as module_0

class Test_Ansible_collector_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        ansible_fact_collector_0 = module_0.AnsibleFactCollector()

if __name__ == "__main__":
    unittest.main()
