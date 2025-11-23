import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            str_0 = ' 6Nc{'
            list_0 = [str_0, str_0]
            str_1 = '|R[Uf'
            dict_0 = {str_1: list_0}
            tuple_0 = (str_0, list_0, dict_0)
            int_0 = 2462
            list_1 = [int_0, int_0]
            set_0 = set()
            file_downloader_0 = module_0.FileDownloader(list_1, set_0)
            var_0 = file_downloader_0.report_destination(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
