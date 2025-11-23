import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0
import collections as module_1

class Test_Collector_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            float_0 = 232.0
            tuple_0 = (float_0,)
            str_0 = '"$-4XLMZ_R|&ZjNQZ'
            var_0 = module_0.select_collector_classes(tuple_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
