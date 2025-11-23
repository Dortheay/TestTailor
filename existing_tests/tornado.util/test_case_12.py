import unittest
import timeout_decorator
import tornado.util as module_0
import builtins as module_1

class Test_Util_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            object_dict_0 = module_0.ObjectDict()
            str_0 = 'Return whether *func* is a coroutine function, i.e. a function\n    wrapped with `~.gen.coroutine`.\n\n    .. versionadded:: 4.5\n    '
            any_0 = module_0.import_object(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
