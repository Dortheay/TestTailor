import unittest
import timeout_decorator
import youtube_dl.extractor.nrk as module_0

class Test_Nrk_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        n_r_k_t_v_i_e_0 = module_0.NRKTVIE()

if __name__ == "__main__":
    unittest.main()
