import unittest
import timeout_decorator
import ansible.module_utils.facts.network.fc_wwn as module_0

class Test_Fc_wwn_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        fc_wwn_initiator_fact_collector_0 = module_0.FcWwnInitiatorFactCollector()

if __name__ == "__main__":
    unittest.main()
