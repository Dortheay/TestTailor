import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            bool_0 = False
            str_0 = 'fVQ'
            field_0 = module_0.Field(description=str_0)
            union_0 = field_0.__or__(field_0)
            any_0 = union_0.validate(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
