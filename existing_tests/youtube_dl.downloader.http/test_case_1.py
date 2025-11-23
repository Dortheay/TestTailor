import unittest
import timeout_decorator
import youtube_dl.downloader.http as module_0

class Test_Http_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'JH1Y\r\\ECiP5h'
        bool_0 = True
        http_f_d_0 = module_0.HttpFD(str_0, bool_0)

if __name__ == "__main__":
    unittest.main()
