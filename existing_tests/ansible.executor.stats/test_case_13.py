import unittest
import timeout_decorator
import ansible.executor.stats as module_0

class Test_Stats_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = False
            aggregate_stats_0 = module_0.AggregateStats()
            int_0 = 2660
            var_0 = aggregate_stats_0.set_custom_stats(bool_0, int_0)
            var_1 = aggregate_stats_0.update_custom_stats(bool_0, bool_0)
            list_0 = None
            var_2 = aggregate_stats_0.decrement(list_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
