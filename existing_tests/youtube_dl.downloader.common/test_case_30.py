import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        try:
            str_0 = "P\x0b'k)39\r*"
            dict_0 = {str_0: str_0}
            file_downloader_0 = module_0.FileDownloader(dict_0, dict_0)
            str_1 = '\n'
            var_0 = file_downloader_0.report_file_already_downloaded(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
