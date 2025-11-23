import unittest
import timeout_decorator
import ansible.module_utils.facts.system.cmdline as module_0

class Test_Cmdline_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        cmd_line_fact_collector_0 = module_0.CmdLineFactCollector()
        var_0 = cmd_line_fact_collector_0.collect()

if __name__ == "__main__":
    unittest.main()
