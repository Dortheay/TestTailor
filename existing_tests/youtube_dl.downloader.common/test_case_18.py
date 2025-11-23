import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            int_0 = -4773
            set_0 = {int_0, int_0}
            str_0 = '0c45586baa71b7cb1d0784ee3f4e00a6'
            str_1 = 'Y@Z'
            bool_0 = False
            file_downloader_0 = module_0.FileDownloader(str_1, bool_0)
            var_0 = file_downloader_0.parse_bytes(str_0)
            int_1 = None
            list_0 = [int_1, int_1, int_1]
            tuple_0 = (list_0,)
            file_downloader_1 = module_0.FileDownloader(tuple_0, int_1)
            var_1 = file_downloader_1.download(int_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
