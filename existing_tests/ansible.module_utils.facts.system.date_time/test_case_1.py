import unittest
import timeout_decorator
import ansible.module_utils.facts.system.date_time as module_0

class Test_Date_time_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        date_time_fact_collector_0 = module_0.DateTimeFactCollector()
        var_0 = date_time_fact_collector_0.collect()

if __name__ == "__main__":
    unittest.main()
