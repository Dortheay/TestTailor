import unittest
import timeout_decorator
import sanic.cookies as module_0

class Test_Cookies_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'query_string'
            bytes_0 = b'\xb3Q\x1d\x8a\xd8\xb0\x94|"\x9f\x99n):\xd8s'
            cookie_jar_0 = module_0.CookieJar(bytes_0)
            var_0 = cookie_jar_0.__delitem__(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
