import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            field_0 = module_0.Field()
            bool_0 = None
            validation_result_0 = field_0.validate_or_error(field_0, strict=bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
