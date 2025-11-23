import unittest
import timeout_decorator
import string_utils.generation as module_0

class Test_Generation_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            int_0 = 320
            str_0 = module_0.random_string(int_0)
            int_1 = 735
            str_1 = module_0.secure_random_hex(int_1)
            int_2 = 4966
            int_3 = 1202
            str_2 = module_0.secure_random_hex(int_3)
            str_3 = module_0.random_string(int_2)
            str_4 = module_0.uuid()
            str_5 = module_0.secure_random_hex(int_0)
            int_4 = None
            str_6 = module_0.random_string(int_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
