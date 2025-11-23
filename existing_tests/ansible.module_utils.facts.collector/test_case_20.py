import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0
import collections as module_1

class Test_Collector_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            str_0 = '\n    Join the original cmd based on manipulations by split_args().\n    This retains the original newlines and whitespaces.\n    '
            str_1 = 'all'
            str_2 = '$'
            dict_0 = {str_0: str_0, str_1: str_1, str_2: str_2}
            var_0 = module_0.tsort(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
