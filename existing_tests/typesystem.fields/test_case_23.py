import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_23(self):
        try:
            int_0 = -1235
            number_0 = module_0.Number(multiple_of=int_0)
            field_0 = None
            object_0 = module_0.Object(property_names=field_0, max_properties=int_0)
            any_0 = object_0.validate(field_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
