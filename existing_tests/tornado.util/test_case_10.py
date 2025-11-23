import unittest
import timeout_decorator
import tornado.util as module_0
import builtins as module_1

class Test_Util_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            callable_0 = None
            str_0 = 'A^qLj8'
            arg_replacer_0 = module_0.ArgReplacer(callable_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
