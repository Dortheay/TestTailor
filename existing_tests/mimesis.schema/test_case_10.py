import unittest
import timeout_decorator
import mimesis.schema as module_0

class Test_Schema_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = 'c['
            abstract_field_0 = module_0.AbstractField()
            int_0 = -1945
            schema_0 = module_0.Schema(abstract_field_0)
            list_0 = schema_0.create(int_0)
            any_0 = abstract_field_0.__call__(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
