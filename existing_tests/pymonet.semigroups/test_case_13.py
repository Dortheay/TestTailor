import unittest
import timeout_decorator
import pymonet.semigroups as module_0

class Test_Semigroups_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'Yvn H:'
            sum_0 = module_0.Sum(str_0)
            max_0 = module_0.Max(sum_0)
            float_0 = -405.0161
            sum_1 = module_0.Sum(float_0)
            dict_0 = {}
            sum_2 = sum_1.concat(sum_1)
            sum_3 = module_0.Sum(dict_0)
            sum_4 = sum_3.concat(sum_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
