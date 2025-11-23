import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_45(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_44(self):
        try:
            bytes_0 = None
            text_0 = module_0.Text()
            array_0 = module_0.Array(text_0)
            any_0 = array_0.serialize(bytes_0)
            bool_0 = True
            str_0 = '-Xi'
            string_0 = module_0.String(allow_blank=bool_0, trim_whitespace=bool_0, format=str_0)
            int_0 = 5
            number_0 = module_0.Number(minimum=int_0, exclusive_minimum=int_0)
            any_1 = number_0.validate(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
