import unittest
import timeout_decorator
import pymonet.semigroups as module_0

class Test_Semigroups_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        set_0 = set()
        min_0 = module_0.Min(set_0)
        last_0 = module_0.Last(min_0)
        max_0 = module_0.Max(last_0)
        one_0 = module_0.One(max_0)
        str_0 = one_0.__str__()

if __name__ == "__main__":
    unittest.main()
