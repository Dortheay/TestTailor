import unittest
import timeout_decorator
import ansible.module_utils.facts.ansible_collector as module_0

class Test_Ansible_collector_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        ansible_fact_collector_0 = module_0.AnsibleFactCollector()
        var_0 = ansible_fact_collector_0.collect()
        bool_0 = None
        list_0 = None
        var_1 = module_0.get_ansible_collector(bool_0, list_0)

if __name__ == "__main__":
    unittest.main()
