import unittest
import timeout_decorator
import thefuck.system.unix as module_0

class Test_Unix_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            var_0 = module_0.getch()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
