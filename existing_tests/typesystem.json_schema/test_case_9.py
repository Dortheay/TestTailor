import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.json_schema as module_1
import typesystem.fields as module_2

class Test_Json_schema_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        str_0 = 'if'
        str_1 = 'then'
        str_2 = 'else'
        str_3 = 'type'
        str_4 = 'minimum'
        str_5 = 'number'
        int_0 = 0
        var_0 = {str_3: str_5, str_4: int_0}
        str_6 = 'maximum'
        int_1 = 100
        var_1 = {str_3: str_5, str_6: int_1}
        str_7 = 'string'
        str_8 = {str_3: str_7}
        var_2 = {str_0: var_0, str_1: var_1, str_2: str_8}
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.if_then_else_from_json_schema(var_2, schema_definitions_0)
        var_3 = field_0.if_clause
        var_4 = field_0.then_clause
        var_5 = field_0.else_clause

if __name__ == "__main__":
    unittest.main()
