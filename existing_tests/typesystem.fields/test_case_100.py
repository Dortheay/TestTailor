import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_101(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        bool_0 = True
        int_0 = None
        object_0 = module_0.Object(additional_properties=bool_0, max_properties=int_0)
        str_0 = 'Must be a valid date format.'
        bool_1 = True
        any_0 = module_0.Any(description=str_0, default=str_0, allow_null=bool_1)
        any_1 = any_0.validate(object_0, bool_0)

if __name__ == "__main__":
    unittest.main()
