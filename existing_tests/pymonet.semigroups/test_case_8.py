import unittest
import timeout_decorator
import pymonet.semigroups as module_0

class Test_Semigroups_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        int_0 = -1618
        max_0 = module_0.Max(int_0)
        var_0 = max_0.concat(max_0)

if __name__ == "__main__":
    unittest.main()
