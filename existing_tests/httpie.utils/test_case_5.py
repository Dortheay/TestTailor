import unittest
import timeout_decorator
import httpie.utils as module_0

class Test_Utils_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'Set-Cookie'
        str_1 = (str_0, str_0)
        str_2 = [str_1, str_1]
        list_0 = module_0.get_expired_cookies(str_2)

if __name__ == "__main__":
    unittest.main()
