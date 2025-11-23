import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.json_schema as module_1
import typesystem.fields as module_2

class Test_Json_schema_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        dict_0 = {}
        str_0 = ''
        dict_1 = {str_0: dict_0, str_0: str_0}
        schema_definitions_0 = module_0.SchemaDefinitions(**dict_1)
        field_0 = module_1.type_from_json_schema(dict_0, schema_definitions_0)
        dict_2 = module_1.get_standard_properties(field_0)

if __name__ == "__main__":
    unittest.main()
