import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.json_schema as module_1
import typesystem.fields as module_2

class Test_Json_schema_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = '$ref'
        str_1 = '#/definitions/Example'
        str_2 = {str_0: str_1}
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.ref_from_json_schema(str_2, schema_definitions_0)

if __name__ == "__main__":
    unittest.main()
