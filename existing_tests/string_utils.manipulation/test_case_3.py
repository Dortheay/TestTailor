import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = ';R'
        bool_0 = module_0.booleanize(str_0)
        str_1 = module_0.shuffle(str_0)
        str_2 = 'P1KC%f\tSjEy87#}b4'
        str_3 = module_0.strip_margin(str_2)
        str_4 = '?\x0c;M*{FzUI7#'
        str_5 = module_0.prettify(str_4)

if __name__ == "__main__":
    unittest.main()
