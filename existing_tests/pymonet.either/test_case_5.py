import unittest
import timeout_decorator
import pymonet.either as module_0
import builtins as module_1

class Test_Either_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        bytes_0 = b'W\xed\xe9@G\xf8\x15\x05iO'
        int_0 = 2661
        either_0 = module_0.Either(int_0)
        list_0 = [either_0, either_0]
        bool_0 = False
        right_0 = module_0.Right(bool_0)
        bool_1 = right_0.is_right()
        var_0 = either_0.is_right()
        left_0 = module_0.Left(list_0)
        var_1 = left_0.bind(bytes_0)

if __name__ == "__main__":
    unittest.main()
