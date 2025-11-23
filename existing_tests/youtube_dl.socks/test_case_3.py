import unittest
import timeout_decorator
import youtube_dl.socks as module_0

class Test_Socks_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            socks5_error_0 = module_0.Socks5Error()
            sockssocket_0 = module_0.sockssocket()
            var_0 = sockssocket_0.connect(socks5_error_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
