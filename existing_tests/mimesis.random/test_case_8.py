import unittest
import timeout_decorator
import mimesis.random as module_0

class Test_Random_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            random_0 = module_0.Random()
            str_0 = random_0.custom_code()
            bytes_0 = random_0.urandom()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
