import unittest
import timeout_decorator
import pymonet.semigroups as module_0

class Test_Semigroups_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        int_0 = True
        map_0 = module_0.Map(int_0)
        str_0 = ''
        first_0 = module_0.First(str_0)
        sum_0 = module_0.Sum(first_0)
        str_1 = sum_0.__str__()
        max_0 = module_0.Max(map_0)
        min_0 = module_0.Min(max_0)
        str_2 = min_0.__str__()
        str_3 = min_0.__str__()

if __name__ == "__main__":
    unittest.main()
