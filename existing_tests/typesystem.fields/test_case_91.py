import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_92(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        optional_0 = None
        str_0 = ','
        string_0 = module_0.String(min_length=optional_0, pattern=str_0)

if __name__ == "__main__":
    unittest.main()
