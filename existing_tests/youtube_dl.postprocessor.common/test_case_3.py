import unittest
import timeout_decorator
import youtube_dl.postprocessor.common as module_0

class Test_Common_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        int_0 = -4114
        post_processor_0 = module_0.PostProcessor()
        dict_0 = None
        var_0 = post_processor_0.run(dict_0)
        var_1 = post_processor_0.run(int_0)
        var_2 = post_processor_0.run(post_processor_0)

if __name__ == "__main__":
    unittest.main()
