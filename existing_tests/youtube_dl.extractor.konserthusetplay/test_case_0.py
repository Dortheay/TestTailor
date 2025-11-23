import unittest
import timeout_decorator
import youtube_dl.extractor.konserthusetplay as module_0

class Test_Konserthusetplay_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        konserthuset_play_i_e_0 = module_0.KonserthusetPlayIE()

if __name__ == "__main__":
    unittest.main()
