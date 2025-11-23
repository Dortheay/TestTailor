import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        schema_definitions_0 = module_0.SchemaDefinitions()
        iterator_0 = schema_definitions_0.__iter__()

if __name__ == "__main__":
    unittest.main()
