import unittest
import timeout_decorator
import tornado.util as module_0
import builtins as module_1

class Test_Util_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'initialized'
            object_dict_0 = module_0.ObjectDict()
            any_0 = object_dict_0.__getattr__(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
