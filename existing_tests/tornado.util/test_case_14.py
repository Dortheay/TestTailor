import unittest
import timeout_decorator
import tornado.util as module_0
import builtins as module_1

class Test_Util_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            base_exception_0 = module_1.BaseException()
            optional_0 = module_0.errno_from_exception(base_exception_0)
            str_0 = 's\\i7\th\x0b=. %b(>_*/+ )'
            str_1 = module_0.re_unescape(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
