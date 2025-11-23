import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.json_schema as module_1
import typesystem.fields as module_2

class Test_Json_schema_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'allOf'
        str_1 = 'default'
        str_2 = 'type'
        str_3 = 'minLength'
        str_4 = 'string'
        int_0 = 2
        var_0 = {str_2: str_4, str_3: int_0}
        str_5 = 'maxLength'
        int_1 = 5
        var_1 = {str_2: str_4, str_5: int_1}
        var_2 = [var_0, var_1]
        str_6 = 'test'
        var_3 = {str_0: var_2, str_1: str_6}
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.all_of_from_json_schema(var_3, schema_definitions_0)
        var_4 = field_0.all_of
        var_5 = len(var_4)
        int_2 = 0
        var_6 = field_0.all_of[int_2]
        int_3 = 1
        var_7 = field_0.all_of[int_3]

if __name__ == "__main__":
    unittest.main()
