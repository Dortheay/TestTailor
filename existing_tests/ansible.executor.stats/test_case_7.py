import unittest
import timeout_decorator
import ansible.executor.stats as module_0

class Test_Stats_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        aggregate_stats_0 = module_0.AggregateStats()
        str_0 = 'test_host'
        str_1 = 'ok'
        var_0 = aggregate_stats_0.increment(str_1, str_0)
        var_1 = aggregate_stats_0.increment(str_1, str_0)

if __name__ == "__main__":
    unittest.main()
