import unittest
import timeout_decorator
import ansible.module_utils.facts.ansible_collector as module_0

class Test_Ansible_collector_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            int_0 = -3085
            ansible_fact_collector_0 = module_0.AnsibleFactCollector()
            var_0 = ansible_fact_collector_0.collect()
            list_0 = [int_0, int_0]
            str_0 = '\ny+yPnnv%tC\x0c'
            collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(str_0)
            bool_0 = False
            bytes_0 = b'71\x1bm'
            str_1 = 'K=$n:QU/'
            tuple_0 = ()
            tuple_1 = (bytes_0, str_1, tuple_0)
            collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector(bool_0, tuple_1)
            collector_meta_data_collector_2 = module_0.CollectorMetaDataCollector(list_0, collector_meta_data_collector_0)
            set_0 = {collector_meta_data_collector_2}
            var_1 = module_0.get_ansible_collector(set_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
