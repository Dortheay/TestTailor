import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_77(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_76(self):
        try:
            int_0 = -1235
            str_0 = 'wJf'
            bool_0 = True
            dict_0 = {}
            string_0 = module_0.String(allow_blank=bool_0, trim_whitespace=bool_0, max_length=int_0, min_length=int_0, pattern=str_0, **dict_0)
            any_0 = string_0.validate(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
