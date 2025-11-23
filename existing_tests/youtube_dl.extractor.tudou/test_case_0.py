import unittest
import timeout_decorator
import youtube_dl.extractor.tudou as module_0

class Test_Tudou_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        tudou_playlist_i_e_0 = module_0.TudouPlaylistIE()

if __name__ == "__main__":
    unittest.main()
