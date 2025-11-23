import unittest
import timeout_decorator
import ansible.executor.stats as module_0

class Test_Stats_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '+'
        complex_0 = None
        aggregate_stats_0 = module_0.AggregateStats()
        var_0 = aggregate_stats_0.update_custom_stats(str_0, complex_0)

if __name__ == "__main__":
    unittest.main()
