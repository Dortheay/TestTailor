import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = '\x0b\nN8,_>g~`&t[OT04!Hb'
            bool_0 = True
            float_0 = 366.3
            dict_0 = {bool_0: float_0, bool_0: float_0}
            tuple_0 = (dict_0,)
            int_0 = 1771
            file_downloader_0 = module_0.FileDownloader(tuple_0, int_0)
            var_0 = file_downloader_0.format_percent(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
