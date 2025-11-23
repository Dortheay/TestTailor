import unittest
import timeout_decorator
import pymonet.either as module_0
import builtins as module_1

class Test_Either_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        object_0 = module_1.object()
        bool_0 = True
        list_0 = [bool_0, bool_0, bool_0, bool_0]
        either_0 = module_0.Either(list_0)
        bool_1 = either_0.__eq__(object_0)
        str_0 = '0?}S\x0c\x0bF|@d}Qfu'
        right_0 = module_0.Right(str_0)
        bool_2 = right_0.is_left()
        var_0 = right_0.to_validation()

if __name__ == "__main__":
    unittest.main()
