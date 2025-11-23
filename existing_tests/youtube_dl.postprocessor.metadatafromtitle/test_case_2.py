import unittest
import timeout_decorator
import youtube_dl.postprocessor.metadatafromtitle as module_0

class Test_Metadatafromtitle_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '%(title)s - %(artist)s'
        metadata_from_title_p_p_0 = module_0.MetadataFromTitlePP(str_0, str_0)

if __name__ == "__main__":
    unittest.main()
