import unittest
import timeout_decorator
import youtube_dl.downloader.common as module_0

class Test_Common_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        tuple_0 = ()
        bytes_0 = b'\xad\xdb\x9a]v'
        int_0 = -1895
        set_0 = {tuple_0, tuple_0, tuple_0, bytes_0}
        file_downloader_0 = module_0.FileDownloader(int_0, set_0)
        bool_0 = True
        bool_1 = True
        var_0 = file_downloader_0.best_block_size(bool_0, bool_1)

if __name__ == "__main__":
    unittest.main()
