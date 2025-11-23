import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            str_0 = None
            var_0 = module_0.url_unescape(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
