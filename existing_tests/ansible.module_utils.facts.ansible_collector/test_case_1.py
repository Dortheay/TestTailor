import unittest
import timeout_decorator
import ansible.module_utils.facts.ansible_collector as module_0

class Test_Ansible_collector_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bytes_0 = b'\xa6\x8e\x15h'
        ansible_fact_collector_0 = module_0.AnsibleFactCollector(bytes_0)
        var_0 = ansible_fact_collector_0.collect()
        dict_0 = {}
        int_0 = -1700
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(int_0)
        collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector(dict_0, collector_meta_data_collector_0)

if __name__ == "__main__":
    unittest.main()
