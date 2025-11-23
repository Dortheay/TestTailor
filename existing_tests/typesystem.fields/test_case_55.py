import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_56(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_55(self):
        try:
            decimal_0 = module_1.Decimal()
            choice_0 = module_0.Choice()
            int_0 = -215
            str_0 = '1uI{'
            string_0 = module_0.String(max_length=choice_0, min_length=int_0, pattern=str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
