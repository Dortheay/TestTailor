import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_81(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_80(self):
        try:
            dict_0 = {}
            bool_0 = True
            str_0 = '-Xi'
            string_0 = module_0.String(allow_blank=bool_0, trim_whitespace=bool_0, format=str_0)
            bool_1 = False
            string_1 = module_0.String(trim_whitespace=bool_1)
            int_0 = 633
            string_2 = module_0.String(min_length=int_0, **dict_0)
            any_0 = string_2.validate(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
