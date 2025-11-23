import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            bool_0 = False
            str_0 = '-Xi'
            string_0 = module_0.String(allow_blank=bool_0, format=str_0)
            any_0 = string_0.validate(bool_0, strict=bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
