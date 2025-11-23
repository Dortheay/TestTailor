import unittest
import timeout_decorator
import youtube_dl.extractor.heise as module_0

class Test_Heise_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        heise_i_e_0 = module_0.HeiseIE()

if __name__ == "__main__":
    unittest.main()
