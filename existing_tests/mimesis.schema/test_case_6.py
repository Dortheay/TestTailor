import unittest
import timeout_decorator
import mimesis.schema as module_0

class Test_Schema_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            abstract_field_0 = module_0.AbstractField()
            schema_0 = module_0.Schema(abstract_field_0)
            list_0 = schema_0.create()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
