import unittest
import timeout_decorator
import mimesis.decorators as module_0

class Test_Decorators_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        callable_0 = module_0.romanize()

if __name__ == "__main__":
    unittest.main()
