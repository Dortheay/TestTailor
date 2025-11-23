import unittest
import timeout_decorator
import pymonet.semigroups as module_0

class Test_Semigroups_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        float_0 = -2603.1
        last_0 = module_0.Last(float_0)

if __name__ == "__main__":
    unittest.main()
