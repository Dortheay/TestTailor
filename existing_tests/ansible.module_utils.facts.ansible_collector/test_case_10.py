import unittest
import timeout_decorator
import ansible.module_utils.facts.ansible_collector as module_0

class Test_Ansible_collector_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bytes_0 = None
            list_0 = [bytes_0, bytes_0, bytes_0]
            collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(bytes_0, list_0)
            ansible_fact_collector_0 = module_0.AnsibleFactCollector()
            int_0 = 126
            bool_0 = False
            int_1 = 1496
            var_0 = collector_meta_data_collector_0.collect(int_1)
            var_1 = ansible_fact_collector_0.collect(list_0)
            float_0 = None
            ansible_fact_collector_1 = module_0.AnsibleFactCollector()
            bytes_1 = None
            float_1 = None
            var_2 = module_0.get_ansible_collector(bytes_1, float_1)
            list_1 = [float_1, bytes_1, float_1]
            var_3 = ansible_fact_collector_0.collect()
            ansible_fact_collector_2 = module_0.AnsibleFactCollector(list_1)
            collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector(int_0, bool_0, float_0)
            str_0 = '5tL@%\\z4wG\x0bYr5!'
            collector_meta_data_collector_2 = module_0.CollectorMetaDataCollector()
            tuple_0 = (list_1,)
            var_4 = module_0.get_ansible_collector(tuple_0, collector_meta_data_collector_2, str_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
