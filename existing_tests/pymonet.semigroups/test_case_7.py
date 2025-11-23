import unittest
import timeout_decorator
import pymonet.semigroups as module_0

class Test_Semigroups_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        int_0 = 6
        min_0 = module_0.Min(int_0)
        int_1 = -13
        min_1 = module_0.Min(int_1)
        var_0 = min_0.concat(min_1)

if __name__ == "__main__":
    unittest.main()
