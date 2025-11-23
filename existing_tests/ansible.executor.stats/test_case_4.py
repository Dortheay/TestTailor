import unittest
import timeout_decorator
import ansible.executor.stats as module_0

class Test_Stats_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        aggregate_stats_0 = module_0.AggregateStats()
        dict_0 = None
        float_0 = -450.195308
        var_0 = aggregate_stats_0.update_custom_stats(dict_0, float_0)
        str_0 = 'failures'
        var_1 = aggregate_stats_0.increment(str_0, str_0)
        var_2 = aggregate_stats_0.decrement(str_0, str_0)
        var_3 = aggregate_stats_0.decrement(str_0, str_0)
        bytes_0 = b'\xdb{\xdb@'
        var_4 = aggregate_stats_0.update_custom_stats(bytes_0, aggregate_stats_0)

if __name__ == "__main__":
    unittest.main()
