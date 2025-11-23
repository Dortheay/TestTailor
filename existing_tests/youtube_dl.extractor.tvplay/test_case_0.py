import unittest
import timeout_decorator
import youtube_dl.extractor.tvplay as module_0

class Test_Tvplay_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        viafree_i_e_0 = module_0.ViafreeIE()

if __name__ == "__main__":
    unittest.main()
