import unittest
import timeout_decorator
import youtube_dl.downloader.hls as module_0

class Test_Hls_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = 508
            bool_0 = None
            str_0 = 'EzZz\rI?\rd?Z58Ymo4X"G'
            bool_1 = False
            hls_f_d_0 = module_0.HlsFD(str_0, bool_1)
            var_0 = hls_f_d_0.real_download(int_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
