import unittest
import timeout_decorator
import youtube_dl.postprocessor.common as module_0

class Test_Common_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        post_processor_0 = module_0.PostProcessor()

if __name__ == "__main__":
    unittest.main()
