import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.json_schema as module_1
import typesystem.fields as module_2

class Test_Json_schema_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        bool_0 = False
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.from_json_schema(bool_0, schema_definitions_0)

if __name__ == "__main__":
    unittest.main()
