import unittest
import timeout_decorator
import sanic.exceptions as module_0

class Test_Exceptions_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        float_0 = 0.001
        bool_0 = False
        invalid_usage_0 = module_0.InvalidUsage(float_0, bool_0)

if __name__ == "__main__":
    unittest.main()
