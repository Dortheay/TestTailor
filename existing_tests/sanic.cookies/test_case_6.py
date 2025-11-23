import unittest
import timeout_decorator
import sanic.cookies as module_0

class Test_Cookies_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'query_string'
            cookie_jar_0 = module_0.CookieJar(str_0)
            cookie_0 = module_0.Cookie(str_0, str_0)
            str_1 = 'expires'
            list_0 = [str_1, cookie_0]
            var_0 = cookie_0.__setitem__(str_1, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
