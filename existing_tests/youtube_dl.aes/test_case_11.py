import unittest
import timeout_decorator
import youtube_dl.aes as module_0

class Test_Aes_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            bytes_0 = b''
            var_0 = module_0.rotate(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
