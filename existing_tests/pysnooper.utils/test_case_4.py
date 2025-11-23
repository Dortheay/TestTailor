import unittest
import timeout_decorator
import pysnooper.utils as module_0

class Test_Utils_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        int_0 = None
        var_0 = module_0.ensure_tuple(int_0)

if __name__ == "__main__":
    unittest.main()
