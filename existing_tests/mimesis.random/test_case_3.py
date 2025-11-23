import unittest
import timeout_decorator
import mimesis.random as module_0

class Test_Random_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        float_0 = -4152.37
        float_1 = -2085.0
        random_0 = module_0.Random()
        float_2 = random_0.uniform(float_0, float_1)
        str_0 = ':checkered_flag:'
        str_1 = random_0.generate_string(str_0)

if __name__ == "__main__":
    unittest.main()
