import unittest
import timeout_decorator
import youtube_dl.downloader.f4m as module_0

class Test_F4m_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            int_0 = -5096
            list_0 = [int_0, int_0, int_0, int_0]
            list_1 = [list_0, list_0, list_0]
            list_2 = [list_1, list_1, list_0]
            int_1 = 1415
            str_0 = 'get_attr'
            dict_0 = {str_0: list_1}
            f4m_f_d_0 = module_0.F4mFD(list_0, dict_0)
            flv_reader_0 = module_0.FlvReader()
            f4m_f_d_1 = module_0.F4mFD(f4m_f_d_0, flv_reader_0)
            var_0 = f4m_f_d_1.real_download(list_2, int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
