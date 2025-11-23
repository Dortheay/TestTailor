import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0

class Test_Collector_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        var_0 = module_0.collector_classes_from_gather_subset()

if __name__ == "__main__":
    unittest.main()
