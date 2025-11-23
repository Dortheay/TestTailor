import unittest
import timeout_decorator
import pymonet.either as module_0
import builtins as module_1

class Test_Either_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        var_0 = None
        right_0 = module_0.Right(var_0)
        var_1 = right_0.to_validation()
        list_0 = [right_0, var_0]
        bool_0 = right_0.is_right()
        str_0 = '\n    Data type for storage any type of function.\n    This function (and all his mappers) will be called only during calling fold method\n    '
        left_0 = module_0.Left(var_0)
        var_2 = left_0.bind(str_0)
        left_1 = module_0.Left(list_0)
        var_3 = left_1.to_validation()
        dict_0 = None
        either_0 = module_0.Either(var_0)
        var_4 = left_1.map(either_0)
        callable_0 = None
        var_5 = left_1.map(callable_0)
        var_6 = left_1.ap(dict_0)

if __name__ == "__main__":
    unittest.main()
