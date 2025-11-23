import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_33(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        try:
            tuple_0 = ()
            bool_0 = None
            list_0 = [tuple_0, tuple_0, tuple_0]
            file_downloader_0 = module_0.FileDownloader(list_0, list_0)
            str_0 = 'yDC?m+'
            bytes_0 = b'^/\xdb\xf3\xf9O\xc7{T\xee\x15z\x8d{s'
            var_0 = file_downloader_0.calc_speed(str_0, bool_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
