import unittest
import timeout_decorator
import sanic.cookies as module_0

class Test_Cookies_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = False
            int_0 = 2498
            cookie_jar_0 = module_0.CookieJar(int_0)
            var_0 = cookie_jar_0.__delitem__(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
