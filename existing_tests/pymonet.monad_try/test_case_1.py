import unittest
import timeout_decorator
import pymonet.monad_try as module_0

class Test_Monad_try_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'tlRey<\\TDZkeAF'
        float_0 = -195.70689
        bool_0 = False
        try_0 = module_0.Try(float_0, bool_0)
        bool_1 = try_0.__eq__(str_0)

if __name__ == "__main__":
    unittest.main()
