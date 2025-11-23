import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            str_0 = 'J|/&'
            float_0 = -1139.5838
            file_downloader_0 = module_0.FileDownloader(str_0, float_0)
            str_1 = 'v80kqp41'
            set_0 = None
            var_0 = file_downloader_0.calc_eta(str_1, set_0, set_0, set_0)
            str_2 = '`6/d!/'
            var_1 = file_downloader_0.report_progress(str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
