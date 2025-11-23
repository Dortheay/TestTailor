import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            int_0 = 2539
            dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
            str_0 = 'h;|@#/*F,M/"&N2d ='
            str_1 = 'y'
            str_2 = 'R1\x0c4p*IL3Q#[;GyM'
            dict_1 = {str_0: str_0, str_1: str_1, str_2: str_1}
            list_0 = [dict_1, dict_1]
            list_1 = None
            file_downloader_0 = module_0.FileDownloader(list_1, str_2)
            list_2 = [file_downloader_0, dict_1, dict_1, str_1]
            file_downloader_1 = module_0.FileDownloader(list_2, list_2)
            file_downloader_2 = module_0.FileDownloader(list_0, file_downloader_1)
            var_0 = file_downloader_2.to_stderr(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
