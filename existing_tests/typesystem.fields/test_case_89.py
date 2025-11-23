import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_90(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        field_0 = module_0.Field()
        union_0 = field_0.__or__(field_0)

if __name__ == "__main__":
    unittest.main()
