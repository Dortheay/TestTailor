import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            float_0 = 5847.951690717487
            str_0 = 'Y@Z'
            str_1 = "D[N%'^\x0bYo-'B Cy%\nh"
            dict_0 = {str_1: float_0, str_1: float_0}
            dict_1 = {}
            tuple_0 = (float_0, str_1, dict_0, dict_1)
            file_downloader_0 = module_0.FileDownloader(tuple_0, dict_0)
            var_0 = file_downloader_0.undo_temp_name(str_0)
            bytes_0 = None
            file_downloader_1 = module_0.FileDownloader(dict_1, dict_1)
            var_1 = file_downloader_1.format_retries(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
