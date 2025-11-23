import unittest
import timeout_decorator
import sanic.cookies as module_0

class Test_Cookies_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'test_cookie'
            str_1 = 'testvale'
            cookie_0 = module_0.Cookie(str_0, str_1)
            bytes_0 = None
            tuple_0 = (bytes_0,)
            dict_0 = {str_1: str_0}
            var_0 = cookie_0.__setitem__(tuple_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
