import unittest
import timeout_decorator
import mimesis.random as module_0

class Test_Random_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            int_0 = 102
            random_0 = module_0.Random()
            str_0 = random_0.randstr(int_0)
            str_1 = 'ENFP'
            any_0 = module_0.get_random_item(str_1)
            str_2 = None
            str_3 = 'Ce'
            random_1 = module_0.Random()
            str_4 = random_1.custom_code(str_1, str_2, str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
