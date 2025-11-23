import unittest
import timeout_decorator
import thefuck.rules.brew_install

class Test_Brew_install_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        pass

if __name__ == "__main__":
    unittest.main()
