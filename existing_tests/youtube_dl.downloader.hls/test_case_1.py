import unittest
import timeout_decorator
import youtube_dl.downloader.hls as module_0

class Test_Hls_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'kqd&'
            int_0 = -1081
            hls_f_d_0 = module_0.HlsFD(str_0, int_0)
            set_0 = {hls_f_d_0}
            var_0 = hls_f_d_0.can_download(str_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
