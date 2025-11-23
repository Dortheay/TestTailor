import unittest
import timeout_decorator
import youtube_dl.postprocessor.common as module_0

class Test_Common_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        int_0 = -2684
        post_processor_0 = module_0.PostProcessor()
        post_processor_1 = module_0.PostProcessor(post_processor_0)
        var_0 = post_processor_1.set_downloader(int_0)

if __name__ == "__main__":
    unittest.main()
