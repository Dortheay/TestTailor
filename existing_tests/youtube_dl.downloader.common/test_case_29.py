import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            dict_0 = None
            set_0 = None
            int_0 = 459
            str_0 = 'Videoaula'
            list_0 = [set_0, dict_0, str_0, str_0]
            file_downloader_0 = module_0.FileDownloader(list_0, list_0)
            list_1 = [str_0, set_0, dict_0, file_downloader_0]
            int_1 = 1424354635
            file_downloader_1 = module_0.FileDownloader(list_1, int_1)
            var_0 = file_downloader_1.report_resuming_byte(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
