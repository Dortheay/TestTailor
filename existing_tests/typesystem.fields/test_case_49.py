import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_50(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_49(self):
        try:
            bool_0 = False
            field_0 = module_0.Field()
            optional_0 = None
            object_0 = module_0.Object(additional_properties=field_0, property_names=field_0, required=optional_0)
            choice_0 = module_0.Choice()
            bytes_0 = b']\xc8\xb1H\xdb\xa2)G\xf8\xe3\xf3\xd3\xa7\xdf\xd2C8\x00'
            array_0 = module_0.Array(field_0, choice_0, bytes_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
