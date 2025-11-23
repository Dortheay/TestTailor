import unittest
import timeout_decorator
import youtube_dl.downloader.f4m as module_0

class Test_F4m_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            list_0 = None
            var_0 = module_0.write_flv_header(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
