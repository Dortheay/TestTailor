import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            dict_0 = {}
            file_downloader_0 = module_0.FileDownloader(dict_0, dict_0)
            var_0 = file_downloader_0.format_eta(file_downloader_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
