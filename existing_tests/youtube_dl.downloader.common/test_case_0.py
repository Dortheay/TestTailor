import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'S4X'
        list_0 = []
        file_downloader_0 = module_0.FileDownloader(str_0, list_0)

if __name__ == "__main__":
    unittest.main()
