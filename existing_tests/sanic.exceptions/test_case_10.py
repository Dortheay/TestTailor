import unittest
import timeout_decorator
import sanic.exceptions as module_0

class Test_Exceptions_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = ";&:]Q-FO8=%2C7'/"
            service_unavailable_0 = module_0.ServiceUnavailable(str_0)
            int_0 = 1152
            var_0 = module_0.abort(int_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
