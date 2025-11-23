import unittest
import timeout_decorator
import youtube_dl.aes as module_0

class Test_Aes_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            int_0 = None
            var_0 = module_0.mix_columns_inv(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
