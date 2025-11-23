import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = '/w'
        str_1 = module_0.slugify(str_0)

if __name__ == "__main__":
    unittest.main()
