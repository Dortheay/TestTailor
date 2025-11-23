import unittest
import timeout_decorator
import youtube_dl.postprocessor.metadatafromtitle as module_0

class Test_Metadatafromtitle_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = False
            str_0 = 'Fs+?N'
            metadata_from_title_p_p_0 = module_0.MetadataFromTitlePP(bool_0, str_0)
            float_0 = None
            var_0 = metadata_from_title_p_p_0.run(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
