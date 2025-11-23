import unittest
import timeout_decorator
import typesystem.json_schema as module_0
import typesystem.schemas as module_1
import typesystem.fields as module_2

class Test_Json_schema_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            dict_0 = None
            str_0 = ''
            bool_0 = False
            schema_definitions_0 = module_1.SchemaDefinitions()
            field_0 = module_0.from_json_schema_type(dict_0, str_0, bool_0, schema_definitions_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
