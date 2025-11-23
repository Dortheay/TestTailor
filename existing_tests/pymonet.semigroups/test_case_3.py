import unittest
import timeout_decorator
import pymonet.semigroups as module_0

class Test_Semigroups_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '6#x:'
        first_0 = module_0.First(str_0)
        list_0 = []
        min_0 = module_0.Min(list_0)
        first_1 = module_0.First(list_0)
        str_1 = first_1.__str__()
        str_2 = first_0.__str__()
        bool_0 = True
        all_0 = module_0.All(bool_0)
        all_1 = module_0.All(list_0)
        all_2 = all_1.concat(all_0)
        str_3 = min_0.__str__()
        max_0 = module_0.Max(first_0)
        str_4 = max_0.__str__()

if __name__ == "__main__":
    unittest.main()
