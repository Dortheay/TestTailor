import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_71(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_70(self):
        try:
            object_0 = module_0.Object()
            str_0 = '#s"e_F\\H,9'
            field_0 = None
            str_1 = "JMi'ohc70~"
            dict_0 = {str_0: field_0, str_1: field_0}
            object_1 = module_0.Object(properties=dict_0, pattern_properties=dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
