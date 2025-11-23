import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_89(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        object_0 = module_0.Object()
        field_0 = module_0.Field()
        any_0 = field_0.get_default_value()

if __name__ == "__main__":
    unittest.main()
