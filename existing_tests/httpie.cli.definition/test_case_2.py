import unittest
import timeout_decorator
import httpie.cli.definition as module_0

class Test_Definition_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = ''
        auth_type_lazy_choices_0 = module_0._AuthTypeLazyChoices()
        var_0 = auth_type_lazy_choices_0.__contains__(str_0)

if __name__ == "__main__":
    unittest.main()
