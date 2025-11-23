import unittest
import timeout_decorator
import youtube_dl.downloader.f4m as module_0

class Test_F4m_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            float_0 = None
            var_0 = module_0.build_fragments_list(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
