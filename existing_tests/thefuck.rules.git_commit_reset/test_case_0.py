import unittest
import timeout_decorator
import thefuck.rules.git_commit_reset as module_0

class Test_Git_commit_reset_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = 0.1
            var_0 = module_0.match(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
