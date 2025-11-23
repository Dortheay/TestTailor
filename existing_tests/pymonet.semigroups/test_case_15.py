import unittest
import timeout_decorator
import pymonet.semigroups as module_0

class Test_Semigroups_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = 710
            max_0 = module_0.Max(int_0)
            var_0 = max_0.concat(max_0)
            dict_0 = {}
            first_0 = module_0.First(dict_0)
            list_0 = []
            last_0 = module_0.Last(list_0)
            one_0 = module_0.One(list_0)
            var_1 = last_0.concat(first_0)
            var_2 = one_0.concat(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
