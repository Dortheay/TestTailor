import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        dict_0 = {}
        file_downloader_0 = module_0.FileDownloader(dict_0, dict_0)
        bool_0 = True
        float_0 = 240.842007
        var_0 = file_downloader_0.slow_down(file_downloader_0, bool_0, float_0)

if __name__ == "__main__":
    unittest.main()
