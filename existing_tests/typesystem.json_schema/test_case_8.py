import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.json_schema as module_1
import typesystem.fields as module_2

class Test_Json_schema_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        bool_0 = True
        field_0 = module_1.from_json_schema(bool_0)
        bool_1 = False
        field_1 = module_1.from_json_schema(bool_1)
        schema_definitions_0 = module_0.SchemaDefinitions()
        str_0 = 'enum'
        str_1 = 'A'
        str_2 = 'B'
        str_3 = 'C'
        str_4 = [str_1, str_2, str_3]
        str_5 = {str_0: str_4}
        field_2 = module_1.from_json_schema(str_5, schema_definitions_0)
        str_6 = '$ref'
        str_7 = '#/definitions/Example'
        str_8 = {str_6: str_7}
        field_3 = module_1.from_json_schema(str_8, schema_definitions_0)
        var_0 = {}
        field_4 = module_1.from_json_schema(var_0)
        str_9 = 'All test cases passed!'
        var_1 = print(str_9)

if __name__ == "__main__":
    unittest.main()
