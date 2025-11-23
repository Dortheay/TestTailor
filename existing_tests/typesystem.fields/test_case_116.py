import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_117(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_31(self):
        str_0 = 'ElLB/4P\\'
        string_0 = module_0.String()
        any_0 = string_0.validate(str_0)

if __name__ == "__main__":
    unittest.main()
