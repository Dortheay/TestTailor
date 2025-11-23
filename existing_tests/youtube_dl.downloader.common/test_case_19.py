import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            int_0 = -824
            list_0 = [int_0, int_0]
            bytes_0 = b'N?\x0cw\xf5\xd3{\x1f'
            file_downloader_0 = module_0.FileDownloader(list_0, bytes_0)
            var_0 = file_downloader_0.report_unable_to_resume()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
