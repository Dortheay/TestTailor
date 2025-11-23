import unittest
import timeout_decorator
import pymonet.monad_try as module_0

class Test_Monad_try_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\x1bP'
            set_0 = set()
            tuple_0 = (bytes_0, set_0)
            float_0 = 608.0
            list_0 = [float_0, float_0]
            bool_0 = True
            try_0 = module_0.Try(list_0, bool_0)
            var_0 = try_0.map(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
