import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_123(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_37(self):
        object_0 = module_0.Object()
        dict_0 = {}
        time_0 = module_0.Time(**dict_0)
        str_0 = ''
        field_0 = None
        dict_1 = {str_0: field_0}
        bool_0 = False
        any_0 = object_0.validate(dict_1, strict=bool_0)

if __name__ == "__main__":
    unittest.main()
