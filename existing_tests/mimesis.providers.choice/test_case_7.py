import unittest
import timeout_decorator
import mimesis.providers.choice as module_0

class Test_Choice_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            optional_0 = None
            choice_0 = module_0.Choice()
            list_0 = [choice_0, optional_0, optional_0]
            bool_0 = True
            str_0 = ''
            list_1 = [bool_0, str_0]
            choice_1 = module_0.Choice()
            var_0 = choice_0.__call__(list_1)
            str_1 = ')r3*q,'
            tuple_0 = (str_1,)
            int_0 = 21
            var_1 = choice_0.__call__(tuple_0, bool_0)
            var_2 = choice_0.__call__(list_0, int_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
