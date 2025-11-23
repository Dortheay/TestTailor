import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '300'
            list_0 = [str_0]
            dict_0 = {}
            bool_0 = False
            bytes_0 = b'|\x06\x00Uq'
            list_1 = [bytes_0, bool_0, str_0, str_0]
            file_downloader_0 = module_0.FileDownloader(bytes_0, list_1)
            file_downloader_1 = module_0.FileDownloader(bool_0, file_downloader_0)
            var_0 = file_downloader_1.calc_percent(list_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
