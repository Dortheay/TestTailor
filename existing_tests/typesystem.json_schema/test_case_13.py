import unittest
import timeout_decorator
import typesystem.json_schema as module_0
import typesystem.schemas as module_1
import typesystem.fields as module_2

class Test_Json_schema_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            dict_0 = {}
            str_0 = ''
            dict_1 = {str_0: str_0, str_0: dict_0}
            schema_definitions_0 = module_1.SchemaDefinitions(**dict_1)
            field_0 = module_0.type_from_json_schema(dict_0, schema_definitions_0)
            tuple_0 = module_0.get_valid_types(dict_0)
            field_1 = module_0.from_json_schema(dict_0)
            dict_2 = module_0.get_standard_properties(field_1)
            dict_3 = module_0.get_standard_properties(field_1)
            var_0 = module_0.to_json_schema(field_0)
            field_2 = module_0.any_of_from_json_schema(dict_0, schema_definitions_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
