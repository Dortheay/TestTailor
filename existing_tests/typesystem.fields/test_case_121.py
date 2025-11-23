import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_122(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_36(self):
        bytes_0 = None
        bool_0 = True
        str_0 = '-Xi'
        string_0 = module_0.String(allow_blank=bool_0, trim_whitespace=bool_0, format=str_0)
        any_0 = string_0.validate(bytes_0)

if __name__ == "__main__":
    unittest.main()
