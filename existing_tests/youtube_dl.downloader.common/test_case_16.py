import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            int_0 = 3613
            set_0 = {int_0}
            tuple_0 = None
            bool_0 = False
            list_0 = [set_0]
            bytes_0 = b'\xf0\x01\xbcAj\xd8\x9aL87}\x0b'
            tuple_1 = (list_0, bool_0, bytes_0)
            file_downloader_0 = module_0.FileDownloader(bool_0, tuple_1)
            var_0 = file_downloader_0.format_speed(tuple_0)
            bytes_1 = b'k\xa0\x97~\xe2\xdc\xdb\xdc\xc6\x9f\x10\xd3NR\xb3]'
            list_1 = [set_0, bytes_1, bytes_1]
            bool_1 = True
            file_downloader_1 = module_0.FileDownloader(tuple_0, bool_1)
            var_1 = file_downloader_1.format_percent(list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
