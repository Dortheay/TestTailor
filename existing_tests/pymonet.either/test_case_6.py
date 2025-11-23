import unittest
import timeout_decorator
import pymonet.either as module_0
import builtins as module_1

class Test_Either_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        dict_0 = {}
        left_0 = module_0.Left(dict_0)
        var_0 = left_0.to_maybe()
        str_0 = 'i3)+B%g}(6b^'
        either_0 = module_0.Either(str_0)

if __name__ == "__main__":
    unittest.main()
