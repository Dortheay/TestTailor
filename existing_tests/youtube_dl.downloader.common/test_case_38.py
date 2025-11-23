import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_39(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_27(self):
        try:
            list_0 = None
            str_0 = 'NotHumpDownHump;'
            file_downloader_0 = module_0.FileDownloader(list_0, str_0)
            var_0 = file_downloader_0.format_percent(list_0)
            str_1 = 'i^;d.'
            dict_0 = {str_1: str_1}
            file_downloader_1 = module_0.FileDownloader(dict_0, dict_0)
            var_1 = file_downloader_1.parse_bytes(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
