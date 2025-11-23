import unittest
import timeout_decorator
import youtube_dl.downloader.ism as module_0

class Test_Ism_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bytes_0 = b'\xe7\x94\xa1(\xf0o$\n\x13\xb5\x97,\xfb\xb5\x10'
            str_0 = 'g(mx\\pw'
            var_0 = module_0.extract_box_data(bytes_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
