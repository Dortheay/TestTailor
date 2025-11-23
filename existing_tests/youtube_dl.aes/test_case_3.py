import unittest
import timeout_decorator
import youtube_dl.aes as module_0

class Test_Aes_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        int_0 = 0
        int_1 = 1
        int_2 = 2
        int_3 = [int_0, int_1, int_2]
        var_0 = module_0.inc(int_3)
        int_4 = 255
        int_5 = [int_0, int_4, int_4]
        var_1 = module_0.inc(int_5)
        int_6 = [int_4, int_4, int_4]
        var_2 = module_0.inc(int_6)
        int_7 = 254
        int_8 = [int_7]
        var_3 = module_0.inc(int_8)
        int_9 = [int_4]
        var_4 = module_0.inc(int_9)

if __name__ == "__main__":
    unittest.main()
