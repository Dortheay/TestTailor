import unittest
import timeout_decorator
import pymonet.monad_try as module_0

class Test_Monad_try_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        set_0 = None
        int_0 = -1016
        bool_0 = False
        try_0 = module_0.Try(int_0, bool_0)
        var_0 = try_0.bind(set_0)

if __name__ == "__main__":
    unittest.main()
