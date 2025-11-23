import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            bytes_0 = b'\x10\x8ay,\xc40\xffm'
            bytes_1 = b'\x06\xb9\xfe\x87\x97\xce\xbc\xf2\xfe\xf8+.\xf4\x9d?S\x84'
            dict_0 = {bytes_1: bytes_1, bytes_1: bytes_1}
            file_downloader_0 = module_0.FileDownloader(bytes_1, dict_0)
            var_0 = file_downloader_0.temp_name(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
