import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            float_0 = 620.49
            list_0 = [float_0]
            schema_0 = module_0.Schema(*list_0)
            iterator_0 = schema_0.__iter__()
            reference_0 = module_0.Reference(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
