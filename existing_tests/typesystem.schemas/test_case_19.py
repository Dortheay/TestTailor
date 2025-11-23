import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        schema_definitions_0 = module_0.SchemaDefinitions()
        schema_0 = module_0.Schema()
        iterator_0 = schema_0.__iter__()
        schema_definitions_0.__setitem__(iterator_0, schema_0)
        str_0 = schema_0.__repr__()
        reference_0 = module_0.Reference(str_0)
        bool_0 = schema_0.__eq__(str_0)
        iterator_1 = schema_definitions_0.__iter__()
        str_1 = schema_0.__repr__()
        str_2 = '\n    Parse and validate a JSON string, rwturning positionally marked error\n    messages on parse or validation failures.\n\n    content - A JSON string or bytestring.\n    validator - A Field instance or Schema class to validate against.\n\n    Returns a two-tuple of (value, error_messages)\n    '
        bool_1 = False
        field_0 = module_1.Field(title=str_2, default=schema_definitions_0, allow_null=bool_1)
        module_0.set_definitions(field_0, schema_definitions_0)
        any_0 = reference_0.serialize(iterator_0)
        int_0 = schema_0.__len__()
        reference_1 = module_0.Reference(str_1)

if __name__ == "__main__":
    unittest.main()
