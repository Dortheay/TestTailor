import unittest
import timeout_decorator
import sanic.exceptions as module_0

class Test_Exceptions_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'Auth required.'
        int_0 = 401
        str_1 = 'Basic'
        str_2 = 'Restricted Area'
        unauthorized_0 = module_0.Unauthorized(str_0, int_0, str_1)
        var_0 = str(unauthorized_0)

if __name__ == "__main__":
    unittest.main()
