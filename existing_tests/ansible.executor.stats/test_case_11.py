import unittest
import timeout_decorator
import ansible.executor.stats as module_0

class Test_Stats_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = "/9\x0c'"
            str_1 = 'defaults_from'
            aggregate_stats_0 = module_0.AggregateStats()
            var_0 = aggregate_stats_0.increment(str_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
