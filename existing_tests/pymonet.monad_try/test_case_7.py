import unittest
import timeout_decorator
import pymonet.monad_try as module_0

class Test_Monad_try_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = 'E&axdgs!Uik '
        bool_0 = False
        try_0 = module_0.Try(str_0, bool_0)
        var_0 = try_0.get()

if __name__ == "__main__":
    unittest.main()
