import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        str_0 = 'MockSchema'
        reference_0 = module_0.Reference(str_0)
        schema_definitions_0 = module_0.SchemaDefinitions()
        module_0.set_definitions(reference_0, schema_definitions_0)
        str_1 = 'NestedSchema'
        reference_1 = module_0.Reference(str_1)

if __name__ == "__main__":
    unittest.main()
