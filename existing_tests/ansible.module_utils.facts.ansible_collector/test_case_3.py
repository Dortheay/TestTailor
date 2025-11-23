import unittest
import timeout_decorator
import ansible.module_utils.facts.ansible_collector as module_0

class Test_Ansible_collector_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'Xo5f\rgN~'
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector()
        dict_0 = {}
        int_0 = -3981
        collector_meta_data_collector_1 = module_0.CollectorMetaDataCollector(dict_0, int_0)
        var_0 = collector_meta_data_collector_0.collect(str_0)

if __name__ == "__main__":
    unittest.main()
