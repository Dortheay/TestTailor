import unittest
import timeout_decorator
import youtube_dl.aes as module_0

class Test_Aes_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            float_0 = -87.395
            str_0 = 'wI\rNB2o`;uT'
            var_0 = module_0.xor(float_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
