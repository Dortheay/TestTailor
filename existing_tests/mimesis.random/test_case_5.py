import unittest
import timeout_decorator
import mimesis.random as module_0

class Test_Random_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'asians'
        random_0 = module_0.Random()
        str_1 = random_0.custom_code(str_0)

if __name__ == "__main__":
    unittest.main()
