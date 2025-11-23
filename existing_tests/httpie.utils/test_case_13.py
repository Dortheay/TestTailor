import unittest
import timeout_decorator
import httpie.utils as module_0

class Test_Utils_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = None
            str_1 = None
            tuple_0 = (str_0, str_1)
            list_0 = [tuple_0, tuple_0, tuple_0, tuple_0]
            float_0 = -533.8
            list_1 = module_0.get_expired_cookies(list_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
