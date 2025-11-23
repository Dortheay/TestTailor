import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_104(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        bool_0 = True
        int_0 = -802
        string_0 = module_0.String(allow_blank=bool_0, min_length=int_0)

if __name__ == "__main__":
    unittest.main()
