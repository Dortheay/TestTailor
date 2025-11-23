import unittest
import timeout_decorator
import youtube_dl.extractor.zdf as module_0

class Test_Zdf_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        z_d_f_i_e_0 = module_0.ZDFIE()

if __name__ == "__main__":
    unittest.main()
