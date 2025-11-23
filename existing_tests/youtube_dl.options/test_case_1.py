import unittest
import timeout_decorator
import youtube_dl.options as module_0

class Test_Options_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        var_0 = module_0.parseOpts()

if __name__ == "__main__":
    unittest.main()
