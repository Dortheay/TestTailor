import unittest
import timeout_decorator
import tornado.util as module_0
import builtins as module_1

class Test_Util_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            list_0 = []
            float_0 = -2176.6138
            dict_0 = None
            tuple_0 = (list_0, float_0, dict_0)
            var_0 = module_0.raise_exc_info(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
