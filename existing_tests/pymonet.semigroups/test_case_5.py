import unittest
import timeout_decorator
import pymonet.semigroups as module_0

class Test_Semigroups_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        float_0 = -1271.13
        one_0 = module_0.One(float_0)
        max_0 = module_0.Max(one_0)
        semigroup_0 = module_0.Semigroup(max_0)
        tuple_0 = None
        int_0 = 567
        tuple_1 = (tuple_0, int_0)
        one_1 = module_0.One(tuple_1)
        var_0 = one_1.concat(semigroup_0)

if __name__ == "__main__":
    unittest.main()
