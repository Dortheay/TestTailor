import unittest
import timeout_decorator
import pymonet.monad_try as module_0

class Test_Monad_try_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = '\n        Take function and applied this function on current box value and returns mapped value.\n\n        :param mapper: mapper function\n        :type mapper: Function(A) -> B\n        :returns: new box with mapped value\n        :rtype: B\n        '
        bool_0 = False
        set_0 = {bool_0, bool_0, bool_0}
        try_0 = module_0.Try(set_0, bool_0)
        var_0 = try_0.filter(str_0)

if __name__ == "__main__":
    unittest.main()
