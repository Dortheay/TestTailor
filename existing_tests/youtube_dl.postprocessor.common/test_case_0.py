import unittest
import timeout_decorator
import youtube_dl.postprocessor.common as module_0

class Test_Common_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            post_processor_0 = module_0.PostProcessor()
            tuple_0 = None
            str_0 = 'appkey=%s&cid=%s&otype=json&%s'
            var_0 = post_processor_0.try_utime(tuple_0, tuple_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
