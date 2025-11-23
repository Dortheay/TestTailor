import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_55(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_54(self):
        try:
            bool_0 = False
            any_0 = module_0.Any(allow_null=bool_0)
            text_0 = module_0.Text()
            optional_0 = None
            string_0 = module_0.String(min_length=text_0, format=optional_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
