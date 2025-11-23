import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '~\\Em@C/_!\x0cSk'
        field_0 = module_1.Field(title=str_0, default=str_0)
        schema_definitions_0 = None
        module_0.set_definitions(field_0, schema_definitions_0)

if __name__ == "__main__":
    unittest.main()
