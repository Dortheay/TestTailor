import unittest
import timeout_decorator
import youtube_dl.extractor.archiveorg as module_0

class Test_Archiveorg_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        archive_org_i_e_0 = module_0.ArchiveOrgIE()

if __name__ == "__main__":
    unittest.main()
