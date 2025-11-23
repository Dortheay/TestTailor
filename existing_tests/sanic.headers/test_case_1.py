import unittest
import timeout_decorator
import sanic.headers as module_0

class Test_Headers_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            dict_0 = None
            str_0 = '74t@\r\x0b-NS '
            optional_0 = module_0.parse_xforwarded(dict_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
