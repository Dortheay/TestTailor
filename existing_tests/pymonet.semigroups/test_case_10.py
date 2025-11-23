import unittest
import timeout_decorator
import pymonet.semigroups as module_0

class Test_Semigroups_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        int_0 = 10
        max_0 = module_0.Max(int_0)
        int_1 = 5
        max_1 = module_0.Max(int_1)
        var_0 = max_0.concat(max_1)
        var_1 = max_0.concat(max_1)

if __name__ == "__main__":
    unittest.main()
