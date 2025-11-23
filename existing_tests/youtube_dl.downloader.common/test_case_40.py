import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_41(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_29(self):
        try:
            tuple_0 = ()
            int_0 = 336
            str_0 = 'BhT7D5;<$Q,'
            file_downloader_0 = module_0.FileDownloader(int_0, str_0)
            bytes_0 = b'\xad\xdb\x9a]v'
            int_1 = -1895
            set_0 = {tuple_0, tuple_0, tuple_0, bytes_0}
            file_downloader_1 = module_0.FileDownloader(int_1, set_0)
            list_0 = [tuple_0, tuple_0]
            var_0 = file_downloader_0.format_eta(int_1)
            str_1 = None
            bool_0 = False
            bool_1 = True
            var_1 = file_downloader_1.best_block_size(bool_0, bool_1)
            dict_0 = {str_0: file_downloader_1, str_1: list_0, str_1: tuple_0, str_1: tuple_0}
            file_downloader_2 = module_0.FileDownloader(list_0, dict_0)
            var_2 = file_downloader_2.download(bytes_0, file_downloader_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
