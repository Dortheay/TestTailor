import unittest
import timeout_decorator
import ansible.module_utils.facts.ansible_collector as module_0

class Test_Ansible_collector_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = "+Wi'"
            collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector()
            float_0 = 177.88
            dict_0 = {str_0: collector_meta_data_collector_0, str_0: float_0}
            ansible_fact_collector_0 = module_0.AnsibleFactCollector(dict_0)
            bytes_0 = b'\xc3\x9b\xef\xebS\xdfO~>e\x14'
            float_1 = 1499.7085
            var_0 = module_0.get_ansible_collector(ansible_fact_collector_0, bytes_0, float_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
