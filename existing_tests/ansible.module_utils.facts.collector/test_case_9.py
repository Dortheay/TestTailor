import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0
import collections as module_1

class Test_Collector_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            bool_0 = True
            bool_1 = True
            set_0 = {bool_1, bool_0, bool_1}
            var_0 = module_0.get_collector_names(bool_0, bool_1, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
