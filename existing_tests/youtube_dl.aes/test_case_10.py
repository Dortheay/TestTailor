import unittest
import timeout_decorator
import youtube_dl.aes as module_0

class Test_Aes_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bytes_0 = b'FC'
            var_0 = module_0.sub_bytes_inv(bytes_0)
            bool_0 = False
            dict_0 = {}
            var_1 = module_0.key_schedule_core(bool_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
