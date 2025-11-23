import unittest
import timeout_decorator
import typesystem.json_schema as module_0
import typesystem.schemas as module_1
import typesystem.fields as module_2

class Test_Json_schema_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            bytes_0 = b'\xe7\xa8\xf4\xdc'
            var_0 = module_0.to_json_schema(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
