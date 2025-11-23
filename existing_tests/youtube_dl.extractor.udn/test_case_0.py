import unittest
import timeout_decorator
import youtube_dl.extractor.udn as module_0

class Test_Udn_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        u_d_n_embed_i_e_0 = module_0.UDNEmbedIE()

if __name__ == "__main__":
    unittest.main()
