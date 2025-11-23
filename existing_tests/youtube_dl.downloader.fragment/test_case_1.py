import unittest
import timeout_decorator
import youtube_dl.downloader.fragment as module_0

class Test_Fragment_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = False
            set_0 = set()
            float_0 = 552.9173
            fragment_f_d_0 = module_0.FragmentFD(set_0, float_0)
            var_0 = fragment_f_d_0.report_skip_fragment(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
