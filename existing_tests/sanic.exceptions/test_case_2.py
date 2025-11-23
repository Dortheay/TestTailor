import unittest
import timeout_decorator
import sanic.exceptions as module_0

class Test_Exceptions_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bool_0 = None
        unauthorized_0 = module_0.Unauthorized(bool_0)
        payload_too_large_0 = module_0.PayloadTooLarge(unauthorized_0)

if __name__ == "__main__":
    unittest.main()
