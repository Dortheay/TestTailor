import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            bool_0 = True
            list_0 = [bool_0, bool_0, bool_0, bool_0]
            str_0 = "P\x0b'k)39\r*"
            dict_0 = {str_0: str_0}
            file_downloader_0 = module_0.FileDownloader(dict_0, dict_0)
            var_0 = file_downloader_0.report_retry(list_0, list_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
