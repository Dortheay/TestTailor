import unittest
import timeout_decorator
import ansible.executor.stats as module_0

class Test_Stats_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        aggregate_stats_0 = module_0.AggregateStats()
        str_0 = 'example_stat'
        int_0 = 10
        str_1 = 'host1'
        var_0 = aggregate_stats_0.update_custom_stats(str_0, int_0, str_1)
        int_1 = 5
        var_1 = aggregate_stats_0.update_custom_stats(str_0, int_1, str_1)
        str_2 = 'key'
        str_3 = 'value'
        str_4 = {str_2: str_3}
        var_2 = aggregate_stats_0.update_custom_stats(str_0, str_4, str_1)
        str_5 = 'another_stat'
        str_6 = 'key1'
        str_7 = 'value1'
        str_8 = {str_6: str_7}
        str_9 = 'host2'
        var_3 = aggregate_stats_0.update_custom_stats(str_5, str_8, str_9)
        str_10 = 'key2'
        str_11 = 'value2'
        str_12 = {str_10: str_11}
        var_4 = aggregate_stats_0.update_custom_stats(str_5, str_12, str_9)
        str_13 = 'global_stat'
        int_2 = 20
        var_5 = aggregate_stats_0.update_custom_stats(str_13, int_2)
        var_6 = aggregate_stats_0.update_custom_stats(str_13, int_1)

if __name__ == "__main__":
    unittest.main()
