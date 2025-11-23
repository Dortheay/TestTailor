import unittest
import timeout_decorator
import semantic_release.ci_checks as module_0

class Test_Ci_checks_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            var_0 = module_0.func_wrapper()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
