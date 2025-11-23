import unittest
import timeout_decorator
import semantic_release.ci_checks as module_0

class Test_Ci_checks_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        var_0 = module_0.check()

if __name__ == "__main__":
    unittest.main()
