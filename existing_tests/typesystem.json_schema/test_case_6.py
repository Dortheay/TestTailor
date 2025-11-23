import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.json_schema as module_1
import typesystem.fields as module_2

class Test_Json_schema_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = '}Y^Pw0(U0zk+'
        str_1 = "#?:gqy_qb3I'-\rv"
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_1: str_1}
        field_0 = module_1.from_json_schema(dict_0)

if __name__ == "__main__":
    unittest.main()
