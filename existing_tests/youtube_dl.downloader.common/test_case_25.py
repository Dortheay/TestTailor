import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            bytes_0 = b'\xdd$\xebF\xf7\x89w\xd5>\x15\x0cC<\xeex'
            str_0 = '-rLwl{Pr49*!'
            dict_0 = {}
            file_downloader_0 = module_0.FileDownloader(str_0, dict_0)
            var_0 = file_downloader_0.ytdl_filename(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
