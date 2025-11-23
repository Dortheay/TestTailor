import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            float_0 = 1663.982
            dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
            file_downloader_0 = module_0.FileDownloader(float_0, dict_0)
            var_0 = file_downloader_0.trouble()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
