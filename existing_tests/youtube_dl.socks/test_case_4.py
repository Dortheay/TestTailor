import unittest
import timeout_decorator
import youtube_dl.socks as module_0

class Test_Socks_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            sockssocket_0 = module_0.sockssocket()
            socks5_error_0 = module_0.Socks5Error()
            var_0 = sockssocket_0.connect_ex(socks5_error_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
