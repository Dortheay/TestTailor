import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            schema_definitions_0 = module_0.SchemaDefinitions()
            schema_0 = module_0.Schema()
            iterator_0 = schema_0.__iter__()
            int_0 = schema_definitions_0.__len__()
            iterator_1 = schema_0.__iter__()
            schema_definitions_0.__setitem__(iterator_0, schema_0)
            str_0 = schema_0.__repr__()
            reference_0 = module_0.Reference(str_0)
            iterator_2 = schema_definitions_0.__iter__()
            reference_1 = module_0.Reference(str_0)
            schema_definitions_0.__setitem__(iterator_0, reference_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
