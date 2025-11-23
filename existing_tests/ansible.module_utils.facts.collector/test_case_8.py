import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0
import collections as module_1

class Test_Collector_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            var_0 = module_0.collector_classes_from_gather_subset()
            str_0 = 'cGLR\n5,A'
            var_1 = module_0.build_dep_data(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
