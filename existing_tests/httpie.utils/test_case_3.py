import unittest
import timeout_decorator
import httpie.utils as module_0

class Test_Utils_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '\n    Convert all bytes args to str\n    by decoding them using stdin encoding.\n\n    '
        tuple_0 = (str_0, str_0)
        list_0 = [tuple_0, tuple_0]
        list_1 = module_0.get_expired_cookies(list_0)

if __name__ == "__main__":
    unittest.main()
