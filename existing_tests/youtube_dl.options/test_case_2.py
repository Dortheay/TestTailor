import unittest
import timeout_decorator
import youtube_dl.options as module_0

class Test_Options_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        list_0 = []
        var_0 = module_0.parseOpts(list_0)

if __name__ == "__main__":
    unittest.main()
