import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_111(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_25(self):
        object_0 = module_0.Object()
        dict_0 = {}
        bool_0 = True
        time_0 = module_0.Time()
        int_0 = 5
        object_1 = module_0.Object(properties=object_0, property_names=time_0, max_properties=int_0, **dict_0)
        any_0 = object_1.validate(dict_0, strict=bool_0)

if __name__ == "__main__":
    unittest.main()
