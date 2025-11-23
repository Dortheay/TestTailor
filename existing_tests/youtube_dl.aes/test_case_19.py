import unittest
import timeout_decorator
import youtube_dl.aes as module_0

class Test_Aes_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            str_0 = ':'
            var_0 = module_0.inc(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
