import unittest
import timeout_decorator
import youtube_dl.downloader.ism as module_0

class Test_Ism_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = ' @8:Z|k8g'
            int_0 = -2723
            bytes_0 = b'de|\xe4\x9b7*\x99s\xe0\x1f\xdf\xa1T\xb7\x08'
            bool_0 = True
            ism_f_d_0 = module_0.IsmFD(bytes_0, bool_0)
            var_0 = ism_f_d_0.real_download(str_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
