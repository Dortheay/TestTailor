import unittest
import timeout_decorator
import typesystem.json_schema as module_0
import typesystem.schemas as module_1
import typesystem.fields as module_2

class Test_Json_schema_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            field_0 = None
            dict_0 = module_0.get_standard_properties(field_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
