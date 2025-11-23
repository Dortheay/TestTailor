import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = '5`\\u:Z([b@tz6S(5etL\\'
            int_0 = 2173
            tuple_0 = ()
            file_downloader_0 = module_0.FileDownloader(int_0, tuple_0)
            var_0 = file_downloader_0.to_console_title(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
