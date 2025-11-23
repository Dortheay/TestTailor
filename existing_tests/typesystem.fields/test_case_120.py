import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_121(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_35(self):
        str_0 = 'o0dG'
        bool_0 = False
        dict_0 = {}
        string_0 = module_0.String(trim_whitespace=bool_0, pattern=str_0, format=str_0, **dict_0)
        any_0 = string_0.validate(str_0, strict=bool_0)

if __name__ == "__main__":
    unittest.main()
