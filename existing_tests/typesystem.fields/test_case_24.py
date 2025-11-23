import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_24(self):
        try:
            array_0 = module_0.Array()
            optional_0 = None
            string_0 = None
            object_0 = module_0.Object(properties=optional_0, additional_properties=array_0, required=string_0)
            any_0 = object_0.validate(optional_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
