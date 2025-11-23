import unittest
import timeout_decorator
import ansible.executor.stats as module_0

class Test_Stats_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        aggregate_stats_0 = module_0.AggregateStats()

if __name__ == "__main__":
    unittest.main()
