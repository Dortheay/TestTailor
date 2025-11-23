import unittest
import timeout_decorator
import string_utils.generation as module_0

class Test_Generation_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            int_0 = None
            str_0 = module_0.secure_random_hex(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
