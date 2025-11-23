import unittest
import timeout_decorator
import pymonet.utils as module_0

class Test_Utils_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            var_0 = module_0.fn()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
