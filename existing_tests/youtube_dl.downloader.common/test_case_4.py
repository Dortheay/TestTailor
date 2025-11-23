import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = None
        dict_0 = {str_0: str_0}
        str_1 = 'aR-{ehDH4{l4gMPo'
        str_2 = 'https://www.vidio.com/auth'
        tuple_0 = ()
        file_downloader_0 = module_0.FileDownloader(str_2, tuple_0)
        bytes_0 = None
        int_0 = -1260
        dict_1 = {bytes_0: str_2, bytes_0: int_0, str_1: dict_0}
        var_0 = file_downloader_0.calc_eta(tuple_0, tuple_0, bytes_0, dict_1)

if __name__ == "__main__":
    unittest.main()
