import unittest
import timeout_decorator
import ansible.executor.stats as module_0

class Test_Stats_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        aggregate_stats_0 = module_0.AggregateStats()
        str_0 = 'failures'
        str_1 = 'host1'
        var_0 = aggregate_stats_0.decrement(str_0, str_1)
        var_1 = aggregate_stats_0.decrement(str_0, str_1)

if __name__ == "__main__":
    unittest.main()
