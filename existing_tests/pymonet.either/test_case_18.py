import unittest
import timeout_decorator
import pymonet.either as module_0
import builtins as module_1

class Test_Either_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            int_0 = True
            float_0 = -2464.24121
            left_0 = module_0.Left(float_0)
            var_0 = left_0.bind(int_0)
            str_0 = '\n        Transform Maybe to Either.\n\n        :returns: Right monad with previous value when Maybe is not empty, in other case Left with None\n        :rtype: Either[A | None]\n        '
            left_1 = module_0.Left(str_0)
            either_0 = module_0.Either(left_1)
            var_1 = either_0.is_right()
            object_0 = module_1.object()
            bool_0 = either_0.__eq__(object_0)
            str_1 = '\n    Data type for storage any type of function.\n    This function (and all his mappers) will be called only during calling fold method\n    '
            right_0 = module_0.Right(str_1)
            list_0 = [var_1, bool_0, object_0, var_1]
            left_2 = module_0.Left(list_0)
            left_3 = module_0.Left(left_1)
            var_2 = left_3.map(right_0)
            var_3 = right_0.to_validation()
            bool_1 = right_0.is_right()
            callable_0 = None
            var_4 = left_3.map(callable_0)
            var_5 = None
            either_1 = module_0.Either(var_5)
            var_6 = left_0.to_maybe()
            left_4 = module_0.Left(var_5)
            var_7 = left_0.ap(object_0)
            either_2 = module_0.Either(var_5)
            callable_1 = None
            var_8 = right_0.case(callable_1, callable_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
