import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            int_0 = -1125
            set_0 = {int_0}
            list_0 = [set_0, set_0]
            str_0 = 'r4d#:8'
            str_1 = '2K\n=lb9"ew&\t\x0c1'
            str_2 = 'q'
            dict_0 = {str_2: str_2, str_2: str_2}
            file_downloader_0 = module_0.FileDownloader(str_1, dict_0)
            var_0 = file_downloader_0.download(list_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
