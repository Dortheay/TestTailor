import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        dict_0 = {}
        schema_0 = module_0.Schema(**dict_0)
        int_0 = schema_0.__len__()

if __name__ == "__main__":
    unittest.main()
