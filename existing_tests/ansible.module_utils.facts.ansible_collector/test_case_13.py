import unittest
import timeout_decorator
import ansible.module_utils.facts.ansible_collector as module_0

class Test_Ansible_collector_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = ' @b\nsARL>r\\U9Z#\t'
            ansible_fact_collector_0 = module_0.AnsibleFactCollector(str_0)
            var_0 = ansible_fact_collector_0.collect()
            var_1 = ansible_fact_collector_0.collect()
            ansible_fact_collector_1 = module_0.AnsibleFactCollector()
            ansible_fact_collector_2 = module_0.AnsibleFactCollector()
            bytes_0 = b''
            set_0 = {bytes_0, bytes_0, bytes_0}
            float_0 = 1429.08323
            int_0 = 3600
            ansible_fact_collector_3 = module_0.AnsibleFactCollector(set_0, float_0, int_0)
            ansible_fact_collector_4 = module_0.AnsibleFactCollector(bytes_0, ansible_fact_collector_3)
            ansible_fact_collector_5 = module_0.AnsibleFactCollector(bytes_0)
            var_2 = ansible_fact_collector_5.collect()
            float_1 = None
            bool_0 = False
            ansible_fact_collector_6 = module_0.AnsibleFactCollector(bool_0)
            bool_1 = False
            collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(ansible_fact_collector_6)
            var_3 = module_0.get_ansible_collector(float_1, float_1)
            var_4 = ansible_fact_collector_1.collect(var_1, bool_1)
            bool_2 = True
            var_5 = ansible_fact_collector_4.collect(int_0, bool_2)
            collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector()
            collector_meta_data_collector_2 = module_0.CollectorMetaDataCollector(collector_meta_data_collector_1)
            collector_meta_data_collector_3 = module_0.CollectorMetaDataCollector(ansible_fact_collector_5, collector_meta_data_collector_2)
            var_6 = ansible_fact_collector_3.collect()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
