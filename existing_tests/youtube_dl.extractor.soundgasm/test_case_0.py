import unittest
import timeout_decorator
import youtube_dl.extractor.soundgasm as module_0

class Test_Soundgasm_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        soundgasm_profile_i_e_0 = module_0.SoundgasmProfileIE()

if __name__ == "__main__":
    unittest.main()
