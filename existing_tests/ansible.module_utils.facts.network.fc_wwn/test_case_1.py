import unittest
import timeout_decorator
import ansible.module_utils.facts.network.fc_wwn as module_0

class Test_Fc_wwn_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        fc_wwn_initiator_fact_collector_0 = module_0.FcWwnInitiatorFactCollector()
        var_0 = fc_wwn_initiator_fact_collector_0.collect()

if __name__ == "__main__":
    unittest.main()
