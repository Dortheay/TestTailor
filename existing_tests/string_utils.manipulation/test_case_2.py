import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = '\x0c9&7n_['
        str_1 = module_0.compress(str_0)

if __name__ == "__main__":
    unittest.main()
