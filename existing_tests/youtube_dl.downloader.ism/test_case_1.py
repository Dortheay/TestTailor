import unittest
import timeout_decorator
import youtube_dl.downloader.ism as module_0

class Test_Ism_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = True
            float_0 = 2563.826
            var_0 = module_0.box(bool_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
