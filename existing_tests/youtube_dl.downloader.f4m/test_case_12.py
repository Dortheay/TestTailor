import unittest
import timeout_decorator
import youtube_dl.downloader.f4m as module_0

class Test_F4m_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            float_0 = 548.98
            bytes_0 = None
            list_0 = [float_0]
            dict_0 = {}
            flv_reader_0 = module_0.FlvReader(**dict_0)
            f4m_f_d_0 = module_0.F4mFD(list_0, flv_reader_0)
            list_1 = [f4m_f_d_0, bytes_0, float_0]
            var_0 = module_0.get_base_url(list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
