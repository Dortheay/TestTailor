import unittest
import timeout_decorator
import mimesis.random as module_0

class Test_Random_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        random_0 = module_0.Random()

if __name__ == "__main__":
    unittest.main()
