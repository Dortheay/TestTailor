import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            int_0 = 3415
            str_0 = ':(<x\roQ}=\t{J7b'
            list_0 = None
            list_1 = [int_0, int_0]
            tuple_0 = ()
            file_downloader_0 = module_0.FileDownloader(list_1, tuple_0)
            var_0 = file_downloader_0.calc_percent(str_0, list_0)
            var_1 = file_downloader_0.report_warning()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
