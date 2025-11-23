import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = '#.\ri9ngT'
            str_1 = 'HS6P,'
            str_2 = '\n        Either:\n\n        value - The validated data.\n\n        Or:\n\n        error - The validation error.\n        '
            list_0 = [str_0]
            str_3 = 'X'
            dict_0 = {str_3: str_0, str_0: list_0, str_1: list_0}
            schema_definitions_0 = module_0.SchemaDefinitions(**dict_0)
            schema_0 = module_0.Schema(*list_0)
            int_0 = schema_0.__len__()
            dict_1 = {str_0: str_0, str_1: str_1, str_1: str_0, str_2: str_1}
            schema_1 = module_0.Schema(**dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
