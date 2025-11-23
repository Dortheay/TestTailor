import unittest
import timeout_decorator
import youtube_dl.downloader.ism as module_0

class Test_Ism_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        bool_0 = False
        float_0 = -1319.1
        ism_f_d_0 = module_0.IsmFD(bool_0, float_0)

if __name__ == "__main__":
    unittest.main()
