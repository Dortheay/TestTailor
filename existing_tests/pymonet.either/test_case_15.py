import unittest
import timeout_decorator
import pymonet.either as module_0
import builtins as module_1

class Test_Either_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            object_0 = module_1.object()
            str_0 = 'ekgAiq'
            left_0 = module_0.Left(str_0)
            list_0 = None
            var_0 = left_0.ap(list_0)
            bool_0 = left_0.is_right()
            callable_0 = None
            str_1 = '\n    Perform right-to-left function composition.\n\n    :param value: argument of first applied function\n    :type value: Any\n    :param functions: list of functions to applied from right-to-left\n    :type functions: List[Function]\n    :returns: result of all functions\n    :rtype: Any\n    '
            right_0 = module_0.Right(str_1)
            var_1 = right_0.map(callable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
