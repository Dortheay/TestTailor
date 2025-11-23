import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0
import collections as module_1

class Test_Collector_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        try:
            str_0 = '10.4'
            str_1 = '5MLl'
            str_2 = ''
            dict_0 = {str_0: str_0, str_1: str_1, str_2: str_0}
            var_0 = module_0.find_unresolved_requires(dict_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
