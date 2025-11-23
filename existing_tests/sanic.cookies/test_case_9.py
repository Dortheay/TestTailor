import unittest
import timeout_decorator
import sanic.cookies as module_0

class Test_Cookies_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'GET'
        cookie_0 = module_0.Cookie(str_0, str_0)

if __name__ == "__main__":
    unittest.main()
