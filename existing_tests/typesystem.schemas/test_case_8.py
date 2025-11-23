import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            dict_0 = {}
            schema_0 = module_0.Schema(**dict_0)
            bool_0 = schema_0.__eq__(schema_0)
            iterator_0 = schema_0.__iter__()
            schema_definitions_0 = module_0.SchemaDefinitions(**dict_0)
            any_0 = schema_0.__getitem__(schema_definitions_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
