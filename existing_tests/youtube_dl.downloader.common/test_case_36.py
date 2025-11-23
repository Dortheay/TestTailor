import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_37(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_25(self):
        try:
            float_0 = 5845.04
            str_0 = 'gDO'
            str_1 = "D[N%'^\x0bYo-'B Cy%\nh"
            float_1 = -363.70035080917705
            dict_0 = {str_0: float_0, str_1: float_1}
            dict_1 = {}
            tuple_0 = (float_1, str_0, dict_0, dict_1)
            file_downloader_0 = module_0.FileDownloader(tuple_0, dict_0)
            var_0 = file_downloader_0.slow_down(dict_1, float_0, str_0)
            bool_0 = True
            file_downloader_1 = module_0.FileDownloader(float_0, bool_0)
            float_2 = -3991.135
            file_downloader_2 = module_0.FileDownloader(dict_0, float_2)
            var_1 = file_downloader_0.format_speed(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
