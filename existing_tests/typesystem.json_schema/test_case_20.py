import unittest
import timeout_decorator
import typesystem.json_schema as module_0
import typesystem.schemas as module_1
import typesystem.fields as module_2

class Test_Json_schema_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            bool_0 = True
            field_0 = module_0.from_json_schema(bool_0)
            bool_1 = False
            field_1 = module_0.from_json_schema(bool_1)
            var_0 = {}
            field_2 = module_0.from_json_schema(var_0)
            schema_definitions_0 = module_1.SchemaDefinitions()
            str_0 = '$ref'
            str_1 = '#/definitions/example'
            str_2 = {str_0: str_1}
            field_3 = module_0.from_json_schema(str_2, schema_definitions_0)
            any_0 = module_2.Any()
            str_3 = 'enum'
            int_0 = 2
            int_1 = 3
            var_1 = [bool_0, int_0, int_1]
            var_2 = {str_3: var_1}
            field_4 = module_0.from_json_schema(var_2)
            var_3 = [bool_0, int_0, int_1]
            choice_0 = module_2.Choice(choices=var_3)
            str_4 = 'const'
            int_2 = 42
            int_3 = {str_4: int_2}
            field_5 = module_0.from_json_schema(int_3)
            const_0 = module_2.Const()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
