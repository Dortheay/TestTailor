import unittest
import timeout_decorator
import youtube_dl.aes as module_0

class Test_Aes_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            str_0 = 'L71i/Ak|-aS)Rc'
            bool_0 = False
            var_0 = module_0.rijndael_mul(str_0, bool_0)
            str_1 = 'bKNZ'
            list_0 = [str_1, str_1]
            tuple_0 = ()
            bytes_0 = b'l\x12\x89\xcd\xd9\xe2\xb9\xee_{o\xe8B\xbcX\x15'
            tuple_1 = (tuple_0, str_1, bytes_0)
            int_0 = 1560273989
            var_1 = module_0.aes_cbc_encrypt(list_0, tuple_1, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
