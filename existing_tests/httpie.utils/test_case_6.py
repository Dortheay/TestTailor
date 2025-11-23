import unittest
import timeout_decorator
import httpie.utils as module_0

class Test_Utils_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = 'Set-Cookie'
        str_1 = (str_0, str_0)
        str_2 = 'csrftoken=def456; Max-Age=60; Path=/;'
        str_3 = (str_0, str_2)
        str_4 = [str_1, str_3]
        explicit_null_auth_0 = module_0.ExplicitNullAuth()
        list_0 = module_0.get_expired_cookies(str_4)

if __name__ == "__main__":
    unittest.main()
