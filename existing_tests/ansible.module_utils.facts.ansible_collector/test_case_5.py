import unittest
import timeout_decorator
import ansible.module_utils.facts.ansible_collector as module_0

class Test_Ansible_collector_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'hardware'
        str_1 = 'network'
        str_2 = [str_0, str_1]
        bool_0 = True
        bool_1 = {str_1: bool_0}
        var_0 = None
        collector_meta_data_collector_0 = module_0.CollectorMetaDataCollector(var_0, var_0, str_2, bool_1)
        var_1 = collector_meta_data_collector_0.collect(var_0, var_0)

if __name__ == "__main__":
    unittest.main()
