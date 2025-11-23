import unittest
import timeout_decorator
import thefuck.rules.choco_install as module_0

class Test_Choco_install_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = -4132
            var_0 = module_0.match(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
