import unittest
import timeout_decorator
import pymonet.monad_try as module_0

class Test_Monad_try_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        bytes_0 = b'u\x89\xa1C}jv\xcc\xb0\x94\x10\x8dp\xc4\x96x2'
        bool_0 = True
        try_0 = module_0.Try(bytes_0, bool_0)

if __name__ == "__main__":
    unittest.main()
