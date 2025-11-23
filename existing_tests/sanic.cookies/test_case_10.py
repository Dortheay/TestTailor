import unittest
import timeout_decorator
import sanic.cookies as module_0

class Test_Cookies_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'query_string'
        cookie_0 = module_0.Cookie(str_0, str_0)
        var_0 = cookie_0.__str__()

if __name__ == "__main__":
    unittest.main()
