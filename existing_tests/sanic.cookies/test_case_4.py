import unittest
import timeout_decorator
import sanic.cookies as module_0

class Test_Cookies_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            float_0 = None
            cookie_jar_0 = module_0.CookieJar(float_0)
            str_0 = 'UVQ'
            dict_0 = {}
            cookie_0 = module_0.Cookie(str_0, dict_0)
            var_0 = cookie_0.encode(cookie_jar_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
