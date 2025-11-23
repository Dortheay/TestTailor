import unittest
import timeout_decorator
import ansible.module_utils.facts.ansible_collector as module_0

class Test_Ansible_collector_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector()
            str_0 = 'PSRP: EXEC %s'
            str_1 = None
            collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector(str_1)
            dict_0 = {collector_meta_data_collector_0: collector_meta_data_collector_0, collector_meta_data_collector_1: str_0, str_1: collector_meta_data_collector_0, str_1: collector_meta_data_collector_0}
            set_0 = {collector_meta_data_collector_1}
            collector_meta_data_collector_2 = module_0.CollectorMetaDataCollector(dict_0, set_0)
            var_0 = collector_meta_data_collector_0.collect(str_0, collector_meta_data_collector_2)
            var_1 = collector_meta_data_collector_0.collect()
            int_0 = -1179
            list_0 = []
            ansible_fact_collector_0 = module_0.AnsibleFactCollector(list_0)
            var_2 = ansible_fact_collector_0.collect()
            tuple_0 = ()
            var_3 = module_0.get_ansible_collector(int_0, ansible_fact_collector_0, tuple_0, list_0, collector_meta_data_collector_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
