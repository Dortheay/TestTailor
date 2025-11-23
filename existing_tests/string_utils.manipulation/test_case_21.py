import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = '`R$U\t8BmkF+q\n'
            str_1 = module_0.asciify(str_0)
            str_2 = 'oXH8Ge\rN\rVo\np\t y\tu'
            bool_0 = module_0.booleanize(str_1)
            var_0 = module_0.camel_case_to_snake(str_2)
            str_3 = '"{}" must be an integer in the range 1-3999'
            str_4 = module_0.decompress(str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
