import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_58(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_57(self):
        try:
            str_0 = '*OiM[2,k'
            field_0 = None
            dict_0 = {str_0: field_0, str_0: field_0}
            float_0 = -1581.041972153826
            object_0 = module_0.Object(pattern_properties=dict_0, required=float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
