import unittest
import timeout_decorator
import sanic.cookies as module_0

class Test_Cookies_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'max-age'
            str_1 = 'ePt;h'
            set_0 = set()
            cookie_jar_0 = module_0.CookieJar(set_0)
            var_0 = cookie_jar_0.__setitem__(str_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
