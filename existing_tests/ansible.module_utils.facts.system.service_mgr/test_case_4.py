import unittest
import timeout_decorator
import ansible.module_utils.facts.system.service_mgr as module_0

class Test_Service_mgr_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = -4602.68
            service_mgr_fact_collector_0 = module_0.ServiceMgrFactCollector(float_0)
            bool_0 = False
            var_0 = service_mgr_fact_collector_0.is_systemd_managed(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
