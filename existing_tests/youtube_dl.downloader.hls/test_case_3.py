import unittest
import timeout_decorator
import youtube_dl.downloader.hls as module_0

class Test_Hls_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            float_0 = None
            bool_0 = False
            str_0 = '[>f_m|W5L'
            dict_0 = {float_0: float_0, str_0: str_0, str_0: float_0}
            dict_1 = {bool_0: float_0}
            int_0 = -1405
            hls_f_d_0 = module_0.HlsFD(dict_1, int_0)
            var_0 = hls_f_d_0.can_download(str_0, dict_0)
            set_0 = {bool_0, bool_0, float_0, bool_0}
            dict_2 = {float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0}
            bytes_0 = b'epb\xfb\xc0_^\xf0\xb5k\x17\x90\x8c\xbb'
            hls_f_d_1 = module_0.HlsFD(dict_2, bytes_0)
            var_1 = hls_f_d_1.can_download(bool_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
