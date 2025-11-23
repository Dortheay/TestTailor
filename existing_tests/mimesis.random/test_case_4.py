import unittest
import timeout_decorator
import mimesis.random as module_0

class Test_Random_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        random_0 = module_0.Random()
        str_0 = random_0.custom_code()

if __name__ == "__main__":
    unittest.main()
