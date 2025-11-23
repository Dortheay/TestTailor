import unittest
import timeout_decorator
import ansible.executor.stats as module_0

class Test_Stats_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        aggregate_stats_0 = module_0.AggregateStats()
        str_0 = 'failures'
        var_0 = aggregate_stats_0.decrement(str_0, str_0)
        float_0 = -484.6
        list_0 = [var_0, var_0]
        bool_0 = False
        var_1 = aggregate_stats_0.update_custom_stats(float_0, list_0, bool_0)

if __name__ == "__main__":
    unittest.main()
