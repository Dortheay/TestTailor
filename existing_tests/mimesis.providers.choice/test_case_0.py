import unittest
import timeout_decorator
import mimesis.providers.choice as module_0

class Test_Choice_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        choice_0 = module_0.Choice()

if __name__ == "__main__":
    unittest.main()
