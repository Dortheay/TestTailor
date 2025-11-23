import unittest
import timeout_decorator
import pymonet.monad_try as module_0

class Test_Monad_try_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            float_0 = -1155.3834
            bytes_0 = b'('
            bool_0 = True
            try_0 = module_0.Try(bytes_0, bool_0)
            var_0 = try_0.filter(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
