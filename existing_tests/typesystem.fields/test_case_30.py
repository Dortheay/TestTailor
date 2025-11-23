import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_30(self):
        try:
            str_0 = ''
            int_0 = -1235
            number_0 = module_0.Number(multiple_of=int_0)
            bool_0 = None
            string_0 = module_0.String(trim_whitespace=bool_0, max_length=int_0, min_length=int_0)
            any_0 = string_0.validate(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
