import unittest
import timeout_decorator
import mimesis.providers.choice as module_0

class Test_Choice_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            optional_0 = None
            int_0 = 1532
            choice_0 = module_0.Choice()
            list_0 = [optional_0, int_0, optional_0]
            bool_0 = True
            var_0 = choice_0.__call__(list_0, bool_0)
            str_0 = '[s])\x0c:y);B\tQ\\~4U~'
            var_1 = choice_0.__call__(str_0)
            var_2 = choice_0.__call__(optional_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
