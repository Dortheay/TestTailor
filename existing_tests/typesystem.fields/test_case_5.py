import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = ''
            string_0 = module_0.String()
            any_0 = string_0.validate(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
