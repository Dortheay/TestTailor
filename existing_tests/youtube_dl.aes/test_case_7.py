import unittest
import timeout_decorator
import youtube_dl.aes as module_0

class Test_Aes_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'QVNkZmdoamtsbW5vcHGxcnR1dnd4eXpBQkNERUZHMTA='
            float_0 = None
            int_0 = -2071
            set_0 = {float_0, str_0}
            tuple_0 = (int_0, set_0, int_0)
            var_0 = module_0.aes_cbc_encrypt(float_0, tuple_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
