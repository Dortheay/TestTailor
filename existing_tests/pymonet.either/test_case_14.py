import unittest
import timeout_decorator
import pymonet.either as module_0
import builtins as module_1

class Test_Either_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bytes_0 = b'\xa7\xae\x00'
            either_0 = module_0.Either(bytes_0)
            object_0 = None
            bool_0 = either_0.__eq__(object_0)
            var_0 = None
            left_0 = module_0.Left(var_0)
            var_1 = left_0.ap(either_0)
            list_0 = [object_0, var_1, bool_0, either_0]
            right_0 = module_0.Right(var_0)
            var_2 = right_0.bind(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
