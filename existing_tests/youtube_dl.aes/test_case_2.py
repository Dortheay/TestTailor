import unittest
import timeout_decorator
import youtube_dl.aes as module_0

class Test_Aes_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        int_0 = -1
        var_0 = lambda block, key: block[::int_0]
        int_1 = 1
        int_2 = 3
        int_3 = 4
        int_4 = 5
        int_5 = [int_1, int_3, int_2, int_3, int_4]
        int_6 = 0
        int_7 = [int_6]
        int_8 = 16
        var_1 = int_7 * int_8
        int_9 = [int_6]
        var_2 = int_9 * int_8
        int_10 = 11
        int_11 = [int_10]
        var_3 = int_11 * int_10
        var_4 = int_5 + var_3
        var_5 = var_4[:int_8]
        var_6 = module_0.xor(var_5, var_2)
        int_12 = -1
        var_7 = var_6[::int_12]
        var_8 = var_7
        var_9 = module_0.aes_cbc_encrypt(int_5, var_1, var_2)

if __name__ == "__main__":
    unittest.main()
