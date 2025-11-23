import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_25(self):
        try:
            dict_0 = {}
            int_0 = 5
            dict_1 = {}
            object_0 = module_0.Object(properties=dict_1, pattern_properties=dict_1, min_properties=int_0)
            any_0 = object_0.validate(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
