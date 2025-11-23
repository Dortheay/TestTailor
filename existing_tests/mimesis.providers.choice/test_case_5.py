import unittest
import timeout_decorator
import mimesis.providers.choice as module_0

class Test_Choice_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            choice_0 = module_0.Choice()
            tuple_0 = ()
            bool_0 = False
            var_0 = choice_0.__call__(tuple_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
