import unittest
import timeout_decorator
import youtube_dl.downloader.f4m as module_0

class Test_F4m_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            bytes_0 = b'\x91\xb2\x93e\xff'
            data_truncated_error_0 = None
            flv_reader_0 = module_0.FlvReader()
            dict_0 = {bytes_0: bytes_0, data_truncated_error_0: data_truncated_error_0, flv_reader_0: data_truncated_error_0}
            tuple_0 = (dict_0,)
            dict_1 = {bytes_0: bytes_0, bytes_0: tuple_0}
            str_0 = 'zSBHN[`|K~'
            f4m_f_d_0 = module_0.F4mFD(str_0, data_truncated_error_0)
            str_1 = "o7%%@5aH*;'w}\r"
            tuple_1 = (dict_1, f4m_f_d_0, str_1)
            var_0 = module_0.write_unsigned_int_24(data_truncated_error_0, tuple_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
