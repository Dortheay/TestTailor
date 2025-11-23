import unittest
import timeout_decorator
import ansible.module_utils.facts.system.service_mgr as module_0

class Test_Service_mgr_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            tuple_0 = None
            service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector()
            var_0 = service_mgr_fact_collector_0.is_systemd_managed_offline(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
