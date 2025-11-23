import unittest
import timeout_decorator
import youtube_dl.extractor.eitb as module_0

class Test_Eitb_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        eitb_i_e_0 = module_0.EitbIE()

if __name__ == "__main__":
    unittest.main()
