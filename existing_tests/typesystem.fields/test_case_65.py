import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_66(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_65(self):
        try:
            int_0 = -1235
            str_0 = '-Xi'
            string_0 = module_0.String(max_length=int_0, min_length=int_0, format=str_0)
            any_0 = string_0.validate(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
