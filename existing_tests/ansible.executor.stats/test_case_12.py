import unittest
import timeout_decorator
import ansible.executor.stats as module_0

class Test_Stats_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = True
            int_0 = 125
            aggregate_stats_0 = module_0.AggregateStats()
            dict_0 = {}
            aggregate_stats_1 = module_0.AggregateStats()
            var_0 = aggregate_stats_1.set_custom_stats(bool_0, dict_0)
            aggregate_stats_2 = module_0.AggregateStats()
            var_1 = aggregate_stats_2.increment(bool_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
