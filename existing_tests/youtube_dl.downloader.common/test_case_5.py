import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        float_0 = -2258.591166636807
        str_0 = 'S4X'
        list_0 = []
        file_downloader_0 = module_0.FileDownloader(str_0, list_0)
        var_0 = file_downloader_0.try_utime(str_0, float_0)

if __name__ == "__main__":
    unittest.main()
