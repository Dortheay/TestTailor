import unittest
import timeout_decorator
import youtube_dl.socks as module_0

class Test_Socks_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        socks5_auth_0 = module_0.Socks5Auth()

if __name__ == "__main__":
    unittest.main()
