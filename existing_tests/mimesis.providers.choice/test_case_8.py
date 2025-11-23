import unittest
import timeout_decorator
import mimesis.providers.choice as module_0

class Test_Choice_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            optional_0 = None
            choice_0 = module_0.Choice()
            list_0 = [choice_0, optional_0, optional_0]
            bool_0 = True
            choice_1 = module_0.Choice()
            choice_2 = module_0.Choice()
            int_0 = 21
            var_0 = choice_0.__call__(list_0, int_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
