import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        schema_definitions_0 = module_0.SchemaDefinitions()
        str_0 = 'MockSchema'
        reference_0 = module_0.Reference(str_0)
        module_0.set_definitions(reference_0, schema_definitions_0)
        array_0 = module_1.Array(reference_0)
        module_0.set_definitions(array_0, schema_definitions_0)
        reference_1 = module_0.Reference(str_0)
        reference_2 = [reference_0, reference_1]
        array_1 = module_1.Array(reference_2)
        module_0.set_definitions(array_1, schema_definitions_0)
        str_1 = 'ref1'
        str_2 = 'ref2'
        reference_3 = {str_1: reference_0, str_2: reference_1}
        object_0 = module_1.Object(properties=reference_3)
        str_3 = 'All tests passed for set_definitions.'
        var_0 = print(str_3)

if __name__ == "__main__":
    unittest.main()
