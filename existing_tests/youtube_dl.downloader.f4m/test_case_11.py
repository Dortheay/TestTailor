import unittest
import timeout_decorator
import youtube_dl.downloader.f4m as module_0

class Test_F4m_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            flv_reader_0 = module_0.FlvReader()
            flv_reader_1 = module_0.FlvReader()
            list_0 = [flv_reader_1, flv_reader_1, flv_reader_1]
            data_truncated_error_0 = module_0.DataTruncatedError(*list_0)
            data_truncated_error_1 = module_0.DataTruncatedError()
            var_0 = module_0.write_metadata_tag(data_truncated_error_1, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
