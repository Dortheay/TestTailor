import unittest
import timeout_decorator
import youtube_dl.downloader.f4m as module_0

class Test_F4m_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            flv_reader_0 = module_0.FlvReader()
            var_0 = flv_reader_0.read_abst()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
