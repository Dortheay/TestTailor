import unittest
import timeout_decorator
import youtube_dl.extractor.glide as module_0

class Test_Glide_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        glide_i_e_0 = module_0.GlideIE()

if __name__ == "__main__":
    unittest.main()
