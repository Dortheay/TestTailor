import unittest
import timeout_decorator
import sanic.cookies as module_0

class Test_Cookies_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '\\=wY\\C'
            cookie_0 = module_0.Cookie(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
