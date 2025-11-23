import unittest
import timeout_decorator
import youtube_dl.downloader.dash as module_0

class Test_Dash_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            dash_segments_f_d_0 = module_0.DashSegmentsFD()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
