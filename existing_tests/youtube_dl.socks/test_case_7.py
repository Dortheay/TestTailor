import unittest
import timeout_decorator
import youtube_dl.socks as module_0

class Test_Socks_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        socks5_error_0 = module_0.Socks5Error()

if __name__ == "__main__":
    unittest.main()
