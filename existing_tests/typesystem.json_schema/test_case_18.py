import unittest
import timeout_decorator
import typesystem.json_schema as module_0
import typesystem.schemas as module_1
import typesystem.fields as module_2

class Test_Json_schema_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            dict_0 = {}
            tuple_0 = module_0.get_valid_types(dict_0)
            field_0 = module_0.from_json_schema(dict_0)
            dict_1 = module_0.get_standard_properties(field_0)
            bytes_0 = b'\x9e\x96W\xa2\xce0\xb2\t\x13T\xb8\n\xab\x91H\xc3\x8c\xefY'
            var_0 = module_0.to_json_schema(field_0)
            var_1 = module_0.to_json_schema(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
