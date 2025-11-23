import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = '%s(%s)'
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
            schema_definitions_0 = module_0.SchemaDefinitions(**dict_0)
            iterator_0 = schema_definitions_0.__iter__()
            schema_0 = module_0.Schema()
            any_0 = schema_0.__getitem__(iterator_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
