import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            schema_0 = module_0.Schema()
            iterator_0 = schema_0.__iter__()
            schema_definitions_0 = module_0.SchemaDefinitions()
            iterator_1 = schema_0.__iter__()
            str_0 = schema_0.__repr__()
            schema_definitions_0.__setitem__(iterator_0, schema_definitions_0)
            reference_0 = module_0.Reference(str_0)
            any_0 = reference_0.validate(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
