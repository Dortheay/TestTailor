import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            str_0 = "$9xE[9R-o'3E["
            set_0 = None
            tuple_0 = (set_0,)
            int_0 = 2798
            bool_0 = False
            file_downloader_0 = module_0.FileDownloader(int_0, bool_0)
            var_0 = file_downloader_0.try_rename(str_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
