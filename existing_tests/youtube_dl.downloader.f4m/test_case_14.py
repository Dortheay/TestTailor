import unittest
import timeout_decorator
import youtube_dl.downloader.f4m as module_0

class Test_F4m_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            complex_0 = None
            int_0 = None
            bool_0 = False
            var_0 = module_0.write_metadata_tag(int_0, bool_0)
            var_1 = module_0.remove_encrypted_media(complex_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
