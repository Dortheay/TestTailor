import unittest
import timeout_decorator
import pymonet.semigroups as module_0

class Test_Semigroups_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = 'a'
        str_1 = 'b'
        int_0 = 3
        sum_0 = module_0.Sum(int_0)
        int_1 = 5
        max_0 = module_0.Max(int_1)
        var_0 = {str_0: sum_0, str_1: max_0}
        map_0 = module_0.Map(var_0)
        int_2 = 7
        sum_1 = module_0.Sum(int_2)
        int_3 = 4
        max_1 = module_0.Max(int_3)
        var_1 = {str_0: sum_1, str_1: max_1}
        map_1 = module_0.Map(var_1)
        var_2 = map_0.concat(map_1)

if __name__ == "__main__":
    unittest.main()
