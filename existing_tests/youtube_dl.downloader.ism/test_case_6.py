import unittest
import timeout_decorator
import youtube_dl.downloader.ism as module_0

class Test_Ism_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'w'
            float_0 = 3233.1
            tuple_0 = None
            list_0 = [str_0, str_0, str_0, str_0]
            dict_0 = {str_0: list_0, str_0: float_0, float_0: list_0, str_0: list_0}
            ism_f_d_0 = module_0.IsmFD(list_0, dict_0)
            var_0 = ism_f_d_0.real_download(dict_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
