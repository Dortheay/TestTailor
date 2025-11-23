import unittest
import timeout_decorator
import youtube_dl.downloader.f4m as module_0

class Test_F4m_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            flv_reader_0 = module_0.FlvReader()
            var_0 = flv_reader_0.read_unsigned_long_long()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
