import unittest
import timeout_decorator
import typesystem.composites as module_0
import typesystem.fields as module_1

class Test_Composites_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'e;1x-GOZ\x0c\x0c9$%C3R/fu'
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
            str_1 = 'D8r!oa3usF)-qHa^~'
            field_0 = module_1.Field(title=str_1)
            list_0 = [field_0, field_0, field_0, field_0]
            all_of_0 = module_0.AllOf(list_0)
            any_0 = all_of_0.validate(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
