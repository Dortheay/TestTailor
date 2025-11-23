import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            schema_definitions_0 = module_0.SchemaDefinitions()
            int_0 = schema_definitions_0.__len__()
            list_0 = [int_0, int_0, schema_definitions_0]
            schema_0 = module_0.Schema(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
