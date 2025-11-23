import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_46(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_45(self):
        try:
            optional_0 = None
            str_0 = 'Cj0m*|ivK`YEd%'
            str_1 = '&LN3nwif8B<yY%'
            any_0 = module_0.Any(title=str_1, description=str_0)
            bool_0 = False
            any_1 = any_0.validate(any_0, bool_0)
            const_0 = module_0.Const(optional_0)
            any_2 = const_0.validate(any_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
