import unittest
import timeout_decorator
import youtube_dl.downloader.dash as module_0

class Test_Dash_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            tuple_0 = ()
            int_0 = 849
            dict_0 = {int_0: int_0, tuple_0: tuple_0, int_0: int_0}
            bool_0 = False
            dash_segments_f_d_0 = module_0.DashSegmentsFD(bool_0, dict_0)
            var_0 = dash_segments_f_d_0.real_download(bool_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
