import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '~"\x0b@@{|d2'
            optional_0 = None
            bool_0 = True
            dict_0 = {str_0: optional_0, str_0: optional_0}
            schema_definitions_0 = module_0.SchemaDefinitions(**dict_0)
            reference_0 = module_0.Reference(str_0, schema_definitions_0)
            any_0 = reference_0.validate(str_0, strict=bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
