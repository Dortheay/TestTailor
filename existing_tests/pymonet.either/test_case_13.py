import unittest
import timeout_decorator
import pymonet.either as module_0
import builtins as module_1

class Test_Either_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            int_0 = 2152
            list_0 = [int_0, int_0]
            either_0 = module_0.Either(list_0)
            var_0 = either_0.to_box()
            str_0 = None
            str_1 = ''
            list_1 = [str_1, str_0, str_0, str_1]
            left_0 = module_0.Left(list_1)
            var_1 = left_0.to_maybe()
            str_2 = 'a\rzjo*:c'
            either_1 = module_0.Either(str_2)
            object_0 = module_1.object()
            right_0 = module_0.Right(object_0)
            var_2 = right_0.to_validation()
            var_3 = either_1.to_try()
            bytes_0 = b'_\x10\xfb\x04 '
            right_1 = module_0.Right(bytes_0)
            var_4 = right_1.to_maybe()
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_1: str_1}
            right_2 = module_0.Right(dict_0)
            var_5 = right_1.map(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
