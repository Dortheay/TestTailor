import unittest
import timeout_decorator
import mimesis.random as module_0

class Test_Random_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            random_0 = module_0.Random()
            str_0 = '@###'
            str_1 = random_0.custom_code(str_0)
            var_0 = len(str_1)
            var_1 = len(str_0)
            int_0 = 0
            var_2 = str_1[int_0]
            var_3 = str_1[int_0]
            int_1 = 1
            var_4 = str_1[int_1:]
            str_2 = '+*++**'
            str_3 = '+'
            str_4 = '*'
            str_5 = random_0.custom_code(str_2, str_3, str_4)
            var_5 = len(str_5)
            var_6 = len(str_2)
            str_6 = '@###'
            str_7 = '@'
            str_8 = random_0.custom_code(str_6, str_7, str_7)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
