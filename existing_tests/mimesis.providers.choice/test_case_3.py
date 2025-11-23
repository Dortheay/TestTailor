import unittest
import timeout_decorator
import mimesis.providers.choice as module_0

class Test_Choice_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            optional_0 = None
            choice_0 = module_0.Choice()
            var_0 = choice_0.__call__(optional_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
