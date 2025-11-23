import unittest
import timeout_decorator
import thefuck.system.unix as module_0

class Test_Unix_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            var_0 = module_0.get_key()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
