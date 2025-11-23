import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_84(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_83(self):
        try:
            bool_0 = False
            dict_0 = {}
            time_0 = module_0.Time(**dict_0)
            int_0 = 5
            object_0 = module_0.Object(additional_properties=bool_0)
            int_1 = 1
            object_1 = module_0.Object(additional_properties=bool_0, min_properties=int_1, max_properties=int_0, **dict_0)
            any_0 = object_1.validate(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
