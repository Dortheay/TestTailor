import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'value1'
        list_0 = [str_0]
        schema_0 = module_0.Schema(*list_0)
        int_0 = schema_0.__len__()

if __name__ == "__main__":
    unittest.main()
