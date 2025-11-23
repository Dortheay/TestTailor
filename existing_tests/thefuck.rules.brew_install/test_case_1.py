import unittest
import timeout_decorator
import thefuck.rules.brew_install as module_0

class Test_Brew_install_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = 1589.75
            var_0 = module_0.match(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
