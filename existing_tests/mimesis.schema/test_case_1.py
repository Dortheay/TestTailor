import unittest
import timeout_decorator
import mimesis.schema as module_0

class Test_Schema_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        abstract_field_0 = module_0.AbstractField()
        var_0 = abstract_field_0.__str__()
        var_1 = abstract_field_0.__str__()
        var_2 = abstract_field_0.__str__()

if __name__ == "__main__":
    unittest.main()
