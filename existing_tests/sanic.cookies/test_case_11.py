import unittest
import timeout_decorator
import sanic.cookies as module_0

class Test_Cookies_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'query_string'
        str_1 = '\\=wY\\C'
        cookie_0 = module_0.Cookie(str_0, str_1)
        var_0 = cookie_0.__str__()

if __name__ == "__main__":
    unittest.main()
