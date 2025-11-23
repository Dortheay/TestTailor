import unittest
import timeout_decorator
import youtube_dl.downloader.f4m as module_0

class Test_F4m_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            flv_reader_0 = module_0.FlvReader()
            var_0 = flv_reader_0.read_afrt()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
