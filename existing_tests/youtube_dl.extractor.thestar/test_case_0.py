import unittest
import timeout_decorator
import youtube_dl.extractor.thestar as module_0

class Test_Thestar_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        the_star_i_e_0 = module_0.TheStarIE()

if __name__ == "__main__":
    unittest.main()
