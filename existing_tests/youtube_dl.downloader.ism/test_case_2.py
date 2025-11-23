import unittest
import timeout_decorator
import youtube_dl.downloader.ism as module_0

class Test_Ism_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = -198
            bytes_0 = b'\xae\x99\xb0\xc9\x0f'
            tuple_0 = (bytes_0,)
            float_0 = 1384.01937
            var_0 = module_0.full_box(int_0, int_0, tuple_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
