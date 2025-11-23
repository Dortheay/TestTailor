import unittest
import timeout_decorator
import tornado.util as module_0
import builtins as module_1

class Test_Util_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            base_exception_0 = None
            optional_0 = module_0.errno_from_exception(base_exception_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
