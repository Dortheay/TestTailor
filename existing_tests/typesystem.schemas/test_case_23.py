import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        schema_definitions_0 = module_0.SchemaDefinitions()
        schema_0 = module_0.Schema()
        iterator_0 = schema_0.__iter__()
        iterator_1 = schema_0.__iter__()
        schema_definitions_0.__setitem__(iterator_0, iterator_0)
        str_0 = schema_0.__repr__()
        reference_0 = module_0.Reference(str_0)
        iterator_2 = schema_definitions_0.__iter__()
        str_1 = schema_0.__repr__()
        iterator_3 = schema_0.__iter__()
        bool_0 = False
        field_0 = module_1.Field(title=str_0, allow_null=bool_0)
        module_0.set_definitions(field_0, schema_definitions_0)
        any_0 = reference_0.serialize(iterator_1)
        bool_1 = schema_0.__eq__(bool_0)
        list_0 = [any_0]
        schema_1 = module_0.Schema(*list_0)
        int_0 = schema_1.__len__()

if __name__ == "__main__":
    unittest.main()
