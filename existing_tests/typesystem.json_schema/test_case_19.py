import unittest
import timeout_decorator
import typesystem.json_schema as module_0
import typesystem.schemas as module_1
import typesystem.fields as module_2

class Test_Json_schema_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            bool_0 = False
            str_0 = 'object'
            field_0 = module_0.from_json_schema(bool_0)
            validation_result_0 = field_0.validate_or_error(bool_0, strict=bool_0)
            bool_1 = False
            var_0 = module_0.to_json_schema(field_0, bool_1)
            dict_0 = {str_0: bool_0, str_0: str_0, validation_result_0: var_0}
            schema_definitions_0 = module_1.SchemaDefinitions()
            field_1 = module_0.if_then_else_from_json_schema(dict_0, schema_definitions_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
