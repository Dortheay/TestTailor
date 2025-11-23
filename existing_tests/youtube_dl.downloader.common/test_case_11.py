import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '='
            bool_0 = True
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
            str_1 = '}]T!Z0N{\t8#VBX'
            dict_1 = {str_1: str_1}
            file_downloader_0 = module_0.FileDownloader(dict_0, dict_1)
            var_0 = file_downloader_0.format_seconds(bool_0)
            bytes_0 = b'\x0b'
            file_downloader_1 = module_0.FileDownloader(str_1, bytes_0)
            var_1 = file_downloader_1.report_warning()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
