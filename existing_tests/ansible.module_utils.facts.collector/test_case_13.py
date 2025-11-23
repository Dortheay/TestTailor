import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0
import collections as module_1

class Test_Collector_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            str_0 = None
            list_0 = []
            dict_0 = {str_0: list_0}
            var_0 = module_0.tsort(dict_0)
            bytes_0 = b'\xc7\xf5\x11s+\xf3\xe5\xb9mZ\x17\xb7U'
            var_1 = module_0.collector_classes_from_gather_subset(list_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
