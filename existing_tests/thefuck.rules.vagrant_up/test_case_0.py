import unittest
import timeout_decorator
import thefuck.rules.vagrant_up as module_0

class Test_Vagrant_up_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = None
            var_0 = module_0.match(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
