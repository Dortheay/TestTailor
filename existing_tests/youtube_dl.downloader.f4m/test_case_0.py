import unittest
import timeout_decorator
import youtube_dl.downloader.f4m as module_0

class Test_F4m_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        list_0 = []
        var_0 = module_0.remove_encrypted_media(list_0)

if __name__ == "__main__":
    unittest.main()
