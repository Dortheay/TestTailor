import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_43(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_31(self):
        try:
            float_0 = -2201.399
            str_0 = "D[N%'^\x0bYo-'B Cy%\nh"
            dict_0 = {str_0: float_0, str_0: float_0}
            dict_1 = {}
            tuple_0 = (float_0, str_0, dict_0, dict_1)
            file_downloader_0 = module_0.FileDownloader(tuple_0, dict_0)
            str_1 = '9X^t"R7c>e'
            var_0 = file_downloader_0.temp_name(str_1)
            var_1 = file_downloader_0.slow_down(dict_1, float_0, str_0)
            float_1 = -222.6688
            int_0 = -339
            var_2 = file_downloader_0.calc_speed(float_1, int_0, str_0)
            float_2 = -1687.0495
            var_3 = file_downloader_0.report_progress(float_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
