import unittest
import timeout_decorator
import pymonet.semigroups as module_0

class Test_Semigroups_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        int_0 = 10
        min_0 = module_0.Min(int_0)
        int_1 = 5
        min_1 = module_0.Min(int_1)
        int_2 = 15
        min_2 = module_0.Min(int_2)
        var_0 = min_0.concat(min_1)
        var_1 = min_0.concat(min_2)
        var_2 = min_1.concat(min_2)

if __name__ == "__main__":
    unittest.main()
