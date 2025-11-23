import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'L{jT}/"'
        bool_0 = False
        str_1 = module_0.snake_case_to_camel(str_0, bool_0)

if __name__ == "__main__":
    unittest.main()
