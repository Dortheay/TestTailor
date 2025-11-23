import unittest
import timeout_decorator
import pymonet.semigroups as module_0

class Test_Semigroups_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = 4040.004
            semigroup_0 = module_0.Semigroup(float_0)
            float_1 = 2225.644133
            first_0 = module_0.First(float_1)
            bool_0 = semigroup_0.__eq__(semigroup_0)
            last_0 = module_0.Last(first_0)
            bool_1 = semigroup_0.__eq__(last_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
