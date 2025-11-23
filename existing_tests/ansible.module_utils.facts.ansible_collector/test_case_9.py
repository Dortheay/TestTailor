import unittest
import timeout_decorator
import ansible.module_utils.facts.ansible_collector as module_0

class Test_Ansible_collector_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            set_0 = None
            ansible_fact_collector_0 = module_0.AnsibleFactCollector()
            dict_0 = {}
            ansible_fact_collector_1 = module_0.AnsibleFactCollector(dict_0)
            var_0 = ansible_fact_collector_1.collect(set_0, ansible_fact_collector_0)
            bytes_0 = b'/\x97k\x12EK\x82\xbck\xfa\xd4'
            var_1 = module_0.get_ansible_collector(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
