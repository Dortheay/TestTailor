import unittest
import timeout_decorator
import typesystem.composites as module_0
import typesystem.fields as module_1

class Test_Composites_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        field_0 = module_1.Field()
        not_0 = module_0.Not(field_0)

if __name__ == "__main__":
    unittest.main()
