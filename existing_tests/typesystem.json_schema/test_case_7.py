import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.json_schema as module_1
import typesystem.fields as module_2

class Test_Json_schema_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = 'not'
        str_1 = 'type'
        str_2 = 'minLength'
        str_3 = 'string'
        int_0 = 5
        var_0 = {str_1: str_3, str_2: int_0}
        var_1 = {str_0: var_0}
        schema_definitions_0 = module_0.SchemaDefinitions()
        bool_0 = False
        string_0 = module_2.String(min_length=int_0)
        field_0 = module_1.not_from_json_schema(var_1, schema_definitions_0)

if __name__ == "__main__":
    unittest.main()
