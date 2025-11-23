import unittest
import timeout_decorator
import ansible.module_utils.facts.ansible_collector as module_0

class Test_Ansible_collector_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        ansible_fact_collector_0 = module_0.AnsibleFactCollector()
        var_0 = ansible_fact_collector_0.collect()

if __name__ == "__main__":
    unittest.main()
