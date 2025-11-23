import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'uYX!b70P+mbx\\s'
        str_1 = module_0.snake_case_to_camel(str_0)
        str_2 = module_0.strip_html(str_0)
        bool_0 = module_0.booleanize(str_2)
        str_3 = module_0.strip_margin(str_0)
        str_4 = module_0.prettify(str_3)
        str_5 = module_0.shuffle(str_3)
        str_6 = 'camel_case_to_snake'
        str_7 = module_0.snake_case_to_camel(str_6)

if __name__ == "__main__":
    unittest.main()
