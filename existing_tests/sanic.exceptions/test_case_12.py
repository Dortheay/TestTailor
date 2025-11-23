import unittest
import timeout_decorator
import sanic.exceptions as module_0

class Test_Exceptions_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            int_0 = 500
            var_0 = module_0.abort(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
