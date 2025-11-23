import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        int_0 = 336
        str_0 = 'BhT7D5;<$Q,'
        file_downloader_0 = module_0.FileDownloader(int_0, str_0)
        int_1 = -1895
        var_0 = file_downloader_0.format_eta(int_1)

if __name__ == "__main__":
    unittest.main()
