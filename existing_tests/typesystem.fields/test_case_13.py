import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            str_0 = 'N'
            boolean_0 = module_0.Boolean()
            bool_0 = True
            any_0 = boolean_0.validate(str_0, strict=bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
