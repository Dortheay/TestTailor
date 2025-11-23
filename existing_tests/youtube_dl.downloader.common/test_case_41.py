import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_42(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_30(self):
        try:
            float_0 = -2201.399
            int_0 = 1432094400
            str_0 = "D[N%'^\x0bYo-'B Cy%\nh"
            dict_0 = {str_0: float_0, str_0: float_0}
            dict_1 = {}
            tuple_0 = (float_0, str_0, dict_0, dict_1)
            file_downloader_0 = module_0.FileDownloader(dict_1, dict_0)
            var_0 = file_downloader_0.format_retries(int_0)
            var_1 = file_downloader_0.slow_down(dict_1, float_0, str_0)
            var_2 = file_downloader_0.add_progress_hook(file_downloader_0)
            str_1 = '/\'u"*#NZ\x0b7Myr'
            complex_0 = None
            var_3 = file_downloader_0.try_utime(tuple_0, complex_0)
            set_0 = set()
            var_4 = file_downloader_0.format_eta(var_1)
            var_5 = file_downloader_0.download(str_1, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
