import unittest
import timeout_decorator
import ansible.module_utils.facts.system.service_mgr as module_0

class Test_Service_mgr_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        dict_0 = {}
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector(dict_0)
        service_mgr_fact_collector_1 = module_0.ServiceMgrFactCollector(service_mgr_fact_collector_0)
        int_0 = -2721
        int_1 = 784
        service_mgr_fact_collector_2 = module_0.ServiceMgrFactCollector()
        var_0 = service_mgr_fact_collector_2.collect(int_0, int_1)

if __name__ == "__main__":
    unittest.main()
