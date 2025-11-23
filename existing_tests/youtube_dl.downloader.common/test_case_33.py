import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_34(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        try:
            list_0 = []
            dict_0 = {}
            float_0 = 3610.31
            str_0 = 'OuQV'
            tuple_0 = (float_0, str_0, list_0)
            file_downloader_0 = module_0.FileDownloader(dict_0, tuple_0)
            file_downloader_1 = module_0.FileDownloader(file_downloader_0, float_0)
            var_0 = file_downloader_1.report_error()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
