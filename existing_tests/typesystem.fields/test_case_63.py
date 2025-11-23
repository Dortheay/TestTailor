import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_64(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_63(self):
        try:
            number_0 = module_0.Number()
            list_0 = []
            str_0 = 'E=dm<*a>5I)\tm'
            field_0 = module_0.Field(description=str_0)
            bool_0 = False
            array_0 = module_0.Array(list_0, field_0, bool_0)
            any_0 = array_0.serialize(number_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
