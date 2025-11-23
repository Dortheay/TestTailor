import unittest
import timeout_decorator
import youtube_dl.extractor.trutv as module_0

class Test_Trutv_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        tru_t_v_i_e_0 = module_0.TruTVIE()

if __name__ == "__main__":
    unittest.main()
