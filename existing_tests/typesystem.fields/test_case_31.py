import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_31(self):
        try:
            int_0 = -1235
            bool_0 = True
            str_0 = '-Xi'
            string_0 = module_0.String(max_length=int_0, min_length=int_0, format=str_0)
            float_0 = None
            any_0 = string_0.serialize(float_0)
            number_0 = module_0.Number(maximum=float_0, exclusive_maximum=int_0)
            any_1 = number_0.validate(bool_0, strict=bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
