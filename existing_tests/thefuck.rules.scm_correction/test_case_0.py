import unittest
import timeout_decorator
import thefuck.rules.scm_correction as module_0

class Test_Scm_correction_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = -479
            var_0 = module_0.match(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
