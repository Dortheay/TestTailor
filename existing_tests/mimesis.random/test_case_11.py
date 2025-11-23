import unittest
import timeout_decorator
import mimesis.random as module_0

class Test_Random_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            random_0 = module_0.Random()
            int_0 = -2117
            any_0 = module_0.get_random_item(int_0, random_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
