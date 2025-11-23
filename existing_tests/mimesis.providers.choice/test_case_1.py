import unittest
import timeout_decorator
import mimesis.providers.choice as module_0

class Test_Choice_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        choice_0 = module_0.Choice()
        str_0 = '[s])\x0c:y);B\tQ\\~4U~'
        var_0 = choice_0.__call__(str_0)

if __name__ == "__main__":
    unittest.main()
