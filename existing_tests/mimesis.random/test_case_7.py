import unittest
import timeout_decorator
import mimesis.random as module_0

class Test_Random_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            random_0 = module_0.Random()
            random_1 = module_0.Random()
            str_0 = random_1.custom_code()
            str_1 = random_1.randstr()
            int_0 = -327
            list_0 = random_0.randints(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
