import unittest
import timeout_decorator
import youtube_dl.extractor.itv as module_0

class Test_Itv_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        i_t_v_b_t_c_c_i_e_0 = module_0.ITVBTCCIE()

if __name__ == "__main__":
    unittest.main()
