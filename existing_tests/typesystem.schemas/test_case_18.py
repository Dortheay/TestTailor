import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        schema_0 = module_0.Schema()
        iterator_0 = schema_0.__iter__()
        str_0 = schema_0.__repr__()

if __name__ == "__main__":
    unittest.main()
