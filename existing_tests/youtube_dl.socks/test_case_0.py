import unittest
import timeout_decorator
import youtube_dl.socks as module_0

class Test_Socks_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            sockssocket_0 = module_0.sockssocket()
            socks5_command_0 = module_0.Socks5Command()
            socks5_error_0 = module_0.Socks5Error(socks5_command_0)
            proxy_0 = module_0.Proxy()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
