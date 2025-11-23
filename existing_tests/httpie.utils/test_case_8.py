import unittest
import timeout_decorator
import httpie.utils as module_0

class Test_Utils_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        str_0 = 'Set-Cookie'
        str_1 = 'sessionid=ab|123; Max-Age=0a Path=/;'
        str_2 = (str_0, str_1)
        str_3 = 'csrftoken=def456; Max-Age=60; Path=/;'
        str_4 = (str_0, str_3)
        str_5 = [str_2, str_4]
        explicit_null_auth_0 = module_0.ExplicitNullAuth()
        list_0 = module_0.get_expired_cookies(str_5)

if __name__ == "__main__":
    unittest.main()
