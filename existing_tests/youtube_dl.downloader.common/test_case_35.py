import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_36(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_24(self):
        try:
            float_0 = -2178.8223385702554
            str_0 = "D[N%'^\x0bYo-'B Cy%\nh"
            dict_0 = {}
            dict_1 = {}
            tuple_0 = (float_0, str_0, dict_0, dict_1)
            file_downloader_0 = module_0.FileDownloader(dict_1, dict_0)
            var_0 = file_downloader_0.slow_down(dict_1, float_0, str_0)
            var_1 = file_downloader_0.add_progress_hook(file_downloader_0)
            bool_0 = True
            str_1 = 'JEb,e\rMV\\|BlM'
            set_0 = {str_0, float_0, bool_0}
            var_2 = file_downloader_0.try_utime(str_1, set_0)
            str_2 = ''
            complex_0 = None
            var_3 = file_downloader_0.try_utime(tuple_0, complex_0)
            set_1 = set()
            var_4 = file_downloader_0.download(str_2, set_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
