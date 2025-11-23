import unittest
import timeout_decorator
import youtube_dl.extractor.hitrecord as module_0

class Test_Hitrecord_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        hit_record_i_e_0 = module_0.HitRecordIE()

if __name__ == "__main__":
    unittest.main()
