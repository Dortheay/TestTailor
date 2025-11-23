import unittest
import timeout_decorator
import string_utils.generation as module_0

class Test_Generation_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = -2222
            str_0 = module_0.random_string(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
