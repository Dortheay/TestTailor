import unittest
import timeout_decorator
import youtube_dl.downloader.http as module_0

class Test_Http_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            dict_0 = {}
            str_0 = '9vB\nyw-G'
            float_0 = -595.9
            bool_0 = False
            http_f_d_0 = module_0.HttpFD(float_0, bool_0)
            var_0 = http_f_d_0.real_download(dict_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
