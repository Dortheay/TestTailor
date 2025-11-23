import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_35(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_23(self):
        try:
            bool_0 = False
            bool_1 = True
            bytes_0 = b'\x91j1O\xfb\x9d\xf3\x91\xd67?R\x91\xae\x13\x8f'
            dict_0 = {bool_1: bool_1, bytes_0: bytes_0, bool_0: bool_1}
            bytes_1 = b')c\x9b\xdf`\xad\xcf<\xda\xe8\xc7'
            tuple_0 = ()
            file_downloader_0 = module_0.FileDownloader(bytes_1, tuple_0)
            var_0 = file_downloader_0.calc_eta(bool_0, bool_1, bytes_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
