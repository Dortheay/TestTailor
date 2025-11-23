import unittest
import timeout_decorator
import ansible.module_utils.facts.ansible_collector as module_0

class Test_Ansible_collector_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector()
            int_0 = -4411
            ansible_fact_collector_0 = module_0.AnsibleFactCollector(int_0)
            var_0 = ansible_fact_collector_0.collect()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
