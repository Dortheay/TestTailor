import unittest
import timeout_decorator
import youtube_dl.downloader.f4m as module_0

class Test_F4m_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            flv_reader_0 = module_0.FlvReader()
            bool_0 = True
            var_0 = module_0.write_metadata_tag(flv_reader_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
