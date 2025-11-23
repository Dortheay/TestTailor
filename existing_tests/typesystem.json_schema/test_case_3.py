import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.json_schema as module_1
import typesystem.fields as module_2

class Test_Json_schema_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'enum'
        str_1 = 'default'
        str_2 = 'A'
        str_3 = 'B'
        str_4 = 'C'
        str_5 = [str_2, str_3, str_4]
        str_6 = {str_0: str_5, str_1: str_3}
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.enum_from_json_schema(str_6, schema_definitions_0)

if __name__ == "__main__":
    unittest.main()
