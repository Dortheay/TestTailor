import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_53(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_52(self):
        try:
            bool_0 = None
            choice_0 = module_0.Choice()
            any_0 = choice_0.validate(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
