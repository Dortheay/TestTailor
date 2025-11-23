import unittest
import timeout_decorator
import pymonet.monad_try as module_0

class Test_Monad_try_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bytes_0 = b'}\xb2\xd7\xed\xad*\x0fg\xb7\nI\xc8\x8c\x8b3\x12'
        set_0 = {bytes_0, bytes_0}
        bool_0 = True
        try_0 = module_0.Try(set_0, bool_0)
        str_0 = try_0.__str__()

if __name__ == "__main__":
    unittest.main()
