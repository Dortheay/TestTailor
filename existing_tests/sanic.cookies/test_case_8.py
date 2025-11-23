import unittest
import timeout_decorator
import sanic.cookies as module_0

class Test_Cookies_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        float_0 = 4141.78
        cookie_jar_0 = module_0.CookieJar(float_0)

if __name__ == "__main__":
    unittest.main()
