import unittest
import timeout_decorator
import mimesis.random as module_0

class Test_Random_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '.charity'
            random_0 = module_0.Random(str_0)
            str_1 = random_0.generate_string(str_0)
            str_2 = random_0.randstr()
            random_1 = module_0.Random()
            bytes_0 = random_1.urandom()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
