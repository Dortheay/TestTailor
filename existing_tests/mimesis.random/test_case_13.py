import unittest
import timeout_decorator
import mimesis.random as module_0

class Test_Random_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            bool_0 = False
            float_0 = 204.8513
            random_0 = module_0.Random()
            float_1 = random_0.uniform(float_0, float_0)
            float_2 = -3954.17829
            any_0 = module_0.get_random_item(bool_0, float_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
