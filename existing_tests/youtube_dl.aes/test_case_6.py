import unittest
import timeout_decorator
import youtube_dl.aes as module_0

class Test_Aes_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'vokA'
            str_1 = "sq^DAxqtX'Pe]|"
            dict_0 = {}
            var_0 = module_0.aes_cbc_decrypt(str_0, str_1, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
