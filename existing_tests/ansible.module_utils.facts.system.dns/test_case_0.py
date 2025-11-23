import unittest
import timeout_decorator
import ansible.module_utils.facts.system.dns as module_0

class Test_Dns_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        dns_fact_collector_0 = module_0.DnsFactCollector()

if __name__ == "__main__":
    unittest.main()
