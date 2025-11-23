import unittest
import timeout_decorator
import youtube_dl.extractor.walla as module_0

class Test_Walla_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        walla_i_e_0 = module_0.WallaIE()

if __name__ == "__main__":
    unittest.main()
