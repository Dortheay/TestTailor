import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_38(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_26(self):
        try:
            float_0 = 5847.951690717487
            int_0 = 1432094400
            str_0 = 'Y@Z'
            str_1 = "D[N%'^\x0bYo-'B Cy%\nh"
            dict_0 = {str_1: float_0, str_1: float_0}
            dict_1 = {}
            tuple_0 = (float_0, str_1, dict_0, dict_1)
            file_downloader_0 = module_0.FileDownloader(tuple_0, dict_0)
            var_0 = file_downloader_0.format_retries(int_0)
            var_1 = file_downloader_0.slow_down(dict_1, float_0, str_0)
            bool_0 = True
            list_0 = []
            list_1 = [list_0, list_0, list_0]
            list_2 = [var_1]
            var_2 = file_downloader_0.format_seconds(int_0)
            file_downloader_1 = module_0.FileDownloader(list_1, list_2)
            int_1 = -489
            float_1 = -432.4
            var_3 = file_downloader_1.calc_eta(int_0, int_1, bool_0, float_1)
            var_4 = file_downloader_1.try_utime(int_1, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
