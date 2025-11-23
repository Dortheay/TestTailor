import unittest
import timeout_decorator
import ansible.executor.stats as module_0

class Test_Stats_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'X10G.iHLQm*&S#>'
        aggregate_stats_0 = module_0.AggregateStats()
        var_0 = aggregate_stats_0.summarize(str_0)
        bytes_0 = b''
        set_0 = {bytes_0, bytes_0}
        aggregate_stats_1 = module_0.AggregateStats()
        var_1 = aggregate_stats_1.update_custom_stats(bytes_0, set_0)

if __name__ == "__main__":
    unittest.main()
