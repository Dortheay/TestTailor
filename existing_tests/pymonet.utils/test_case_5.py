import unittest
import timeout_decorator
import pymonet.utils as module_0

class Test_Utils_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        int_0 = True
        int_1 = module_0.increase(int_0)
        int_2 = module_0.increase(int_0)

if __name__ == "__main__":
    unittest.main()
