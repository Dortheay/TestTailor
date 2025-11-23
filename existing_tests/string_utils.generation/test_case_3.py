import unittest
import timeout_decorator
import string_utils.generation as module_0

class Test_Generation_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            int_0 = -1613
            str_0 = module_0.secure_random_hex(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
