import unittest
import timeout_decorator
import youtube_dl.downloader.f4m as module_0

class Test_F4m_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            bytes_0 = b'\x06\x19J\xddf\xa6\xe5\x08\x1f\xb1wj\x15\xc2go'
            list_0 = [bytes_0]
            flv_reader_0 = module_0.FlvReader(*list_0)
            var_0 = module_0.write_flv_header(flv_reader_0)
            flv_reader_1 = module_0.FlvReader(*list_0)
            var_1 = flv_reader_1.read_string()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
