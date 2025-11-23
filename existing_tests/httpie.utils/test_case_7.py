import unittest
import timeout_decorator
import httpie.utils as module_0

class Test_Utils_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = 'Set-Cookie'
        str_1 = 'sessionid=abc123; Max-Age=0; Path=/;'
        str_2 = (str_0, str_1)
        str_3 = 'csrftoken=def456; Max-yge=60; Path=/;'
        str_4 = (str_0, str_3)
        str_5 = [str_2, str_4]
        list_0 = module_0.get_expired_cookies(str_5)

if __name__ == "__main__":
    unittest.main()
