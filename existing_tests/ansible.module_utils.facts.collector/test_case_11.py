import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0
import collections as module_1

class Test_Collector_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            float_0 = 60.0
            list_0 = [float_0, float_0, float_0]
            var_0 = module_0.collector_classes_from_gather_subset(float_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
