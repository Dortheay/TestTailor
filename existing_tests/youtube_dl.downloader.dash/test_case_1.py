import unittest
import timeout_decorator
import youtube_dl.downloader.dash as module_0

class Test_Dash_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = 2135.616182
            str_0 = 'b\x0c%qS\nz=J'
            float_1 = 896.0
            str_1 = '(https?://[^/]+\\.simplecast\\.com)'
            dash_segments_f_d_0 = module_0.DashSegmentsFD(float_1, str_1)
            var_0 = dash_segments_f_d_0.real_download(float_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
