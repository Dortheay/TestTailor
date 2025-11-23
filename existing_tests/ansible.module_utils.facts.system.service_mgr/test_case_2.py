import unittest
import timeout_decorator
import ansible.module_utils.facts.system.service_mgr as module_0

class Test_Service_mgr_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector()
        var_0 = service_mgr_fact_collector_0.collect()
        list_0 = []
        var_1 = service_mgr_fact_collector_0.collect(list_0, service_mgr_fact_collector_0)

if __name__ == "__main__":
    unittest.main()
