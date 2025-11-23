import unittest
import timeout_decorator
import ansible.module_utils.facts.system.dns as module_0

class Test_Dns_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        dns_fact_collector_0 = module_0.DnsFactCollector()
        var_0 = dns_fact_collector_0.collect()

if __name__ == "__main__":
    unittest.main()
