import unittest
import timeout_decorator
import mimesis.random as module_0

class Test_Random_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = '2us/'
            random_0 = module_0.Random()
            any_0 = module_0.get_random_item(str_0, random_0)
            random_1 = module_0.Random()
            str_1 = random_1.custom_code(str_0)
            any_1 = module_0.get_random_item(str_0)
            random_2 = module_0.Random()
            str_2 = '\x0b\n=s;uXlTH?A.0M'
            str_3 = random_0.generate_string(str_2)
            str_4 = random_2.custom_code()
            str_5 = random_2.randstr()
            bool_0 = None
            dict_0 = {str_0: random_2, str_2: any_1}
            list_0 = []
            list_1 = [any_0, list_0, any_1, dict_0]
            str_6 = random_2.randstr(bool_0, list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
