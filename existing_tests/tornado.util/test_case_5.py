import unittest
import timeout_decorator
import tornado.util as module_0
import builtins as module_1

class Test_Util_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'Test exception'
            var_0 = ValueError(str_0)
            var_1 = None
            var_2 = (var_1, var_1, var_1)
            var_3 = module_0.raise_exc_info(var_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
