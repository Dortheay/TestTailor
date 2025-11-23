import unittest
import timeout_decorator
import httpie.cli.definition as module_0

class Test_Definition_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        auth_type_lazy_choices_0 = module_0._AuthTypeLazyChoices()

if __name__ == "__main__":
    unittest.main()
